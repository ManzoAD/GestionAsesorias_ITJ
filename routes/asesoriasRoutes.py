from flask import Blueprint,render_template,request,session,redirect
from db.mongoOnline import MongoOnline
from flask_login import login_required

#Definir el blueprint para clientes
asesoria = Blueprint('asesoria',__name__)

#Definir la ruta de categorias
@asesoria.route('/asesorias')
@login_required
def consultar_categorias():
    #print(session['id'])
    if session:
        objMongo = MongoOnline()
        objMongo.conexion_mongoOnline()
        datAseso=objMongo.datos_Asesoria_card()
        datComment= objMongo.datos_comentarios()
        secciones =objMongo.secciones_Asesoria()
        objMongo.desconexion_mongoOnline()
        return render_template('mobInicio.html',datos=datAseso,seccionar=secciones,comentar=datComment)
    else:
        return redirect('/login')


@asesoria.route('/asesorias/comentario',methods=['POST','GET'])
def ingresar_comentario():
    valores = request.form["comUs"]
    print(valores)
    objMongo = MongoOnline()
    objMongo.insertar_Comentario(valores)
    datAseso=objMongo.datos_Asesoria_card()
    datComment= objMongo.datos_comentarios()
    secciones =objMongo.secciones_Asesoria()
    return  render_template('mobInicio.html',datos=datAseso,seccionar=secciones,comentar=datComment)
    