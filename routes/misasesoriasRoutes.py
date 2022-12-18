from flask import Blueprint,render_template,session,redirect,flash,request
from flask_login import login_required
from db.mongoOnline import MongoOnline
#Definir el blueprint para clientes
misAseso = Blueprint('misAseso',__name__)

#Definir la ruta de categorias
@misAseso.route('/misAsesorias')
@login_required
def consultar_estadistica():
    objMong= MongoOnline()
    objMong.conexion_mongoOnline()
    dat_user=objMong.obtener_usuario(session["_user_id"])
    
    
    if len(dat_user[0])>0:
        dat_aseso = objMong.obtener_AsesoriasUsuario(dat_user[0]["data_asesorias"]) #Validar nulos?
        if session['rol']=="Estudiante":
            objMong.desconexion_mongoOnline()
            return render_template('asesorias.html',datUs=dat_user[0],datAs=dat_aseso)

        elif session['rol']=="Docente":
            
            objMong.desconexion_mongoOnline()
            return render_template('docente.html',datUs=dat_user[0],datAs=dat_aseso)

        elif session['rol']=="Admin":
            datDoc=objMong.obtener_docentes()
            print('---------------------')
            print(datDoc)
            print('----------------------')
            objMong.desconexion_mongoOnline()
            return render_template('admin.html',datUs=dat_user[0],datDoce=datDoc)
    flash("Ha ocurrido un error con tus datos")
    objMong.desconexion_mongoOnline()
    return redirect('/asesorias')


@misAseso.route('/misAsesorias/docenteAseso',methods=['GET','POST'])
def docente_asesoria():
    #{'nom_Aseso':'Simulacion','clas_Aseso':'Programacion'}
    #nomb_Aseso / clas_Aseso / cap_Aseso / fchIni_Aseso / fchFin_Aseso / Lun_hi / Lun_hf
    values=request.form.to_dict()
    for i in values.values():
        print(i)
        if i=="" or i==0 or i == None or i=="Docente" or i=="Clasificaciones":
            flash("Error: El formulario debe ir completo")
            return redirect('/misAsesorias')
    
    objM= MongoOnline()
    objM.conexion_mongoOnline()

    #Obtenemos el idDocente
    atrib={'_id':0,'id_usuario':1}
    filt={'nombre_usuario':values['nom_Doce']}
    idDoc=objM.consulta_mongodbOnline("Usuarios",filt,atrib)
    #Obtenemos la longitud de todas las asesorias
    atrib={'_id':0}
    filt={}
    longi=objM.consulta_mongodbOnline("Asesorias",filt,atrib)
    idAs=f"as{len(longi)+1}"

    #Generamos nuestro diccionario para Asignar la asesoria al docente
    datos={'id_asesoria':idAs,"nombre_asesoria":values['nom_Aseso']}
    hora=objM.limpiarHorario(values['Lun_hi'],values['Lun_hf'],values['Mar_hi'],values['Mar_hf'],values['Mie_hi'],values['Mie_hf'],values['Jue_hi'],values['Jue_hf'],values['Vie_hi'],values['Vie_hf'])
    if hora is not None:
        horario=objM.FormarHorario(hora,values['aula_Aseso'])
        asignado=objM.AsignarAsesoria(datos,idDoc[0]['id_usuario'])
        print()

        if "Error" in asignado:
            flash(asignado)
            objM.desconexion_mongoOnline()
            return redirect('/misAsesorias')
        else:
            #print('Asignado-------------------------')
            #print(asignado)
            #print('---------------------------------')
            #Comenzamos a  general el horario de la asesoria
            
            datos={
            "id_asesoria": idAs,
            "nombre_asesoria": values['nom_Aseso'],
            "docente": {
            "id_usuario": idDoc[0]['id_usuario'],
            "nombre": values["nom_Doce"]
            },
            "alumnos": [],
            "horario": horario,
            "Espacios_disponibles": int(values["cap_Aseso"]),
            "Temario": [],
            "id_estadistica": "",
            "inscritos": 0,
            "Area": values['clas_Aseso'],
            "Periodo":{"Inicio":values["fchIni_Aseso"],"Fin":values["fchFin_Aseso"]}
            }
            respuesta= objM.insertar("Asesorias",datos)
            if respuesta:
                flash('Asesaria Creada con exito')
            else:
                flash('Fallo en la creacion de Asesoria')
    else:
        flash("Error formato horario: Debe contener Inicio/Fin ")
    objM.desconexion_mongoOnline()
    return redirect('/misAsesorias')

@misAseso.route('/misAsesorias/avisos',methods=['GET','POST'])
def avisar():
    #msj_asunto / msj_descripcion
    values = request.form.to_dict()
    objM= MongoOnline()
    objM.conexion_mongoOnline()
    avi=objM.nuevoAviso(values['msj_asunto'],values['msj_descripcion'])
    if avi:
        flash("Aviso enviado con exito!!!")
    else:
        flash("Fallo en  envio del aviso")
    objM.desconexion_mongoOnline()

    return redirect('/misAsesorias')


