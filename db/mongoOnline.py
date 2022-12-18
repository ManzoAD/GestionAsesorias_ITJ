import pymongo
import bcrypt
class MongoOnline:
    def __init__(self):
        self.MONGO_DATABASE = "Gestion_Asesorias"
        self.MONGO_URI = 'mongodb+srv://m4nz0diego386:LPG186mongo01@cluster0.hj6tahj.mongodb.net/?retryWrites=true&w=majority'
        self.MONGO_CLIENT =None
        self.MONGO_RESPUESTA= None
        self.MONGO_TIMEOUT=10000

    def conexion_mongoOnline(self):
        try:
            self.MONGO_CLIENT =pymongo.MongoClient(self.MONGO_URI,serverSelectionTimeoutMS=self.MONGO_TIMEOUT)
        except Exception as error:
            print("Error:",error)
        else:
            pass
            #print("Conexion al servidor realizada")

    def desconexion_mongoOnline(self):
         if self.MONGO_CLIENT:
            self.MONGO_CLIENT.close()

#Consulta general de la asesoria
    def consulta_mongodbOnline(self,tabla,filtro,atributos={"_id":0}):
        response =[]
        self.MONGO_RESPUESTA= self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].find(filtro,atributos)
        if self.MONGO_RESPUESTA:
            for reg in self.MONGO_RESPUESTA:
                response.append(reg)
        return response

#Actualizacion general de la asesoria
    def ActualizarDocuments(self,tabla,filtro,nuevos_valores):
        self.MONGO_RESPUESTA= self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].update_many(filtro,nuevos_valores)
        if self.MONGO_RESPUESTA:
            return True
            #return self.MONGO_RESPUESTA
        return False
#-------------------------------------Consultas
#Consultas especificas
    def datos_Asesoria_card(self):
        atribu={"_id":0,"id_asesoria":1,"nombre_asesoria":1,"docente":1,"horario":1,"Area":1,"Temario":1,"Espacios_disponibles":1}
        filtro={}
        respuesta= self.consulta_mongodbOnline("Asesorias",filtro,atribu)
        return respuesta

    def obtener_usuario(self,id_usuario):
        atribu={"_id":0,"id_usuario":1,"correo":1,"clave":1,"data_asesorias":1,"nombre_usuario":1}
        filtro={"id_usuario":id_usuario}
        respuesta= self.consulta_mongodbOnline("Usuarios",filtro,atribu)
        if respuesta:
            return respuesta
        return None

    def obtener_docentes(self):
        atribu={"_id":0,"id_usuario":1,"nombre_usuario":1}
        filtro={"rol":"Docente"}
        respuesta= self.consulta_mongodbOnline("Usuarios",filtro,atribu)
        if respuesta:
            return respuesta
        return None

    def obtener_AsesoriasUsuario(self,all_asesoDat):
        respuestas=[]
        if len(all_asesoDat[0])>0:
            for i in all_asesoDat:
                filtro={"id_asesoria":i['id_asesoria']}
                dat=self.consulta_mongodbOnline("Asesorias",filtro)
                if dat is not None:
                    respuestas.append(dat[0])
        else:
            respuestas.append({"Error": "hay un error"})
        return respuestas




        #filtro={"id_asesoria":id_asesoria}
        #respuesta = self.consulta_mongodbOnline("Asesorias",filtro)
        #if respuesta is not None:
         #   return respuesta[0]
        return None



    def datos_comentarios(self):
        filtro={}
        respuesta= self.consulta_mongodbOnline("Comentarios",filtro)
        return respuesta


    def secciones_Asesoria(self):
        secciones=[]
        atribu={"_id":0,"Area":1}
        filtro={}
        respuesta= self.consulta_mongodbOnline("Asesorias",filtro,atribu)
        for i in respuesta:
            if(i["Area"] not in secciones):
                secciones.append(i["Area"])
        return secciones
    
    def validarLogin(self,dtos):
        filtro={"correo":dtos['mail_login'],"rol":dtos["RadioSesion"]}
        atributos={"_id":0,"id_usuario":1,"correo":1,"rol":1,"clave":1}
        valor = self.consulta_mongodbOnline("Usuarios",filtro,atributos)
        datos={}
        if valor:
            ClaveC=self.validarClave(dtos['clave_form'],valor[0]['clave'])
            if ClaveC:
                datos={
                "id_usuario":valor[0]["id_usuario"],
                "correo":valor[0]["correo"],
                "rol":valor[0]["rol"],
                "clave":valor[0]["clave"]
                }
        return datos

    def validarClave(self,clave,clavecif):
        if(bcrypt.checkpw((clave).encode('utf-8'),(clavecif).encode('utf-8'))):
            return True
        else:
            return False

    def generarTokem(self,datos):
        print()

#-----------------------------------------Inserciones de los valores
#---------------------------------------Insercion General
    def insertar(self,tabla,documento):
        self.MONGO_RESPUESTA= self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].insert_one(documento)
        if self.MONGO_RESPUESTA:
            return self.MONGO_RESPUESTA
        else:
            return None

    def insertar_Comentario(self,descrip="",idCom="c20",nomUsu="Diego Manzo",idUS="us01"):
            respuesta={}
            documento={
                "id_comentario":idCom,
                "descripcion":descrip,
                "reacciones":[],
                "c_usuario":[{"id_usuario":idUS,"nombre":nomUsu}]
            }
            self.MONGO_RESPUESTA= self.MONGO_CLIENT[self.MONGO_DATABASE]["Comentarios"].insert_one(documento)
            if self.MONGO_RESPUESTA:
                respuesta["resultado"]="Comentario Ingresado con exito!!!"
                print("Valido")
            else:
                respuesta["resultado"]="Error comentario no ingresado!!!!"
                print("no valido")
                
    def nuevoUsuario(self,datos):
        filtro={}
        self.conexion_mongoOnline()
        canti= self.consulta_mongodbOnline("Usuarios",filtro)
        formId= f"us{len(canti)+1}"
        valCryp= self.encryptar(datos["clave"])
        documento={
            "id_usuario":formId,
            "nombre_usuario":datos["nombre_usuario"],
            "correo":datos["correo"],
            "rol":datos["rol"],
            "data_asesorias":[{}],
            "clave":str(valCryp),
            "avatar":"default.jpg",
            "activo":True
        }
        self.MONGO_RESPUESTA= self.MONGO_CLIENT[self.MONGO_DATABASE]["Usuarios"].insert_one(documento)
        if self.MONGO_RESPUESTA:
            return"Insercion Exitosa"
        else:
            return "Error en insercion"
    
    def encryptar(self,valor):
        sal = bcrypt.gensalt()
        contra_cifrada = bcrypt.hashpw(valor.encode('utf-8'),sal)
        return contra_cifrada.decode('utf-8')

    #Le asignamos la asesoria al docente
    def AsignarAsesoria(self,datos,id_usuario):
        #debemos recibir el id_usuarios, id_asesoria, nombre_asesoria
        filtro={"id_usuario":id_usuario}
        atributos={"_id":0,"data_asesorias":1,"nombre_usuario":1,"rol":1}
        consu =self.consulta_mongodbOnline("Usuarios",filtro,atributos)
        nodup=self.noduplicados(datos['id_asesoria'],consu[0]['data_asesorias'])
        if  nodup: #validamos que no duplique la asesoria
            consu=self.consulta_mongodbOnline("Usuarios",filtro,atributos)
            if len(consu[0]['data_asesorias'])==3: #Validamos que no exceda el maximo de asesorias
                return "Error: Numero de Asesorias Permitido (3)"
            else:
                #Evitamos el cruce en los horarios datos-->nuevaAsesoria consu-->todas las asesorias
                self.EvitarCruces(datos,consu[0]['data_asesorias'])
                nuevoVal={'$push':{'data_asesorias':
                {
                    "id_asesoria":datos['id_asesoria'],
                    "nombre_asesoria":datos["nombre_asesoria"]
                    }}}
                actual=self.ActualizarDocuments("Usuarios",filtro,nuevoVal)
                if actual:
                    #Asignamos los alumnos a la asesoria
                    if consu['rol']=="Estudiante":
                        aaa=self.InscribirAlumnos(datos['id_asesoria'],id_usuario,consu['nombre_usuario'])
                        if aaa==False:
                            return "Fallo en la asignacion del usuario"
                    return "Asignacion de Asesoria Exitosa"
                else:
                    return "Error en la asignacion , intentalo mas tarde"
        else:
            return "Error: Intento de doble asignacion"

    def InscribirAlumnos(self,id_asesoria,id_usuario,nombre_usuario):
        filtro={"id_asesoria":id_asesoria}
        alumno={'id_usuario':id_usuario,'nombre_usuario':nombre_usuario}
        nuevoVal={'$push':{'alumnos':alumno}}
        actuali=self.ActualizarDocuments("Asesorias",filtro,nuevoVal)
        return actuali
    
    def EvitarCruces(self,NWasesoria,datos_asesorias):
        print('--------------------------------')
        print('--------------------------------')
        for i in datos_asesorias:
            filtro={"id_asesoria":i['id_asesoria']}
            atributos={'_id':0,'horario':1}
            val=self.consulta_mongodbOnline("Asesorias",filtro,atributos)
            """ for i in val[0]:
                if i['HoraFin']== """
        pass

    #Creamos la asesoria
    def CrearAsesoria(self,datos):
        pass


    def limpiarHorario(self,*args):
        lista=[]
        cont=0
        for i in range (0,len(args)):
            cont+=1
            if cont%2==0: #comparamos
                if args[i]!="00:00" and args[i-1]!="00:00":
                    print(args[i-1],"-",args[i])
                    lista.append({'Dia':self.Dias(cont),'HoraInicio':args[i-1],"HoraFin":args[i]})
                elif args[i]!="00:00" or args[i-1]!="00:00":
                    return None
        return lista
    def FormarHorario(self,horas,aula):
        listaHorario=[]
        for i in horas:
            listaHorario.append({'Dia':i['Dia'],'Aula':aula,'HoraFin':i['HoraFin'],'HoraInicio':i['HoraInicio']})
        return listaHorario


    def Dias(self,numPar):
        if numPar ==2:
            return "Lunes"
        elif numPar == 4:
            return "Martes"
        elif numPar == 6:
            return "Miercoles"
        elif numPar == 8:
            return "Jueves"
        elif numPar == 10:
            return "Viernes"
        return "Fallo"

    def noduplicados(self,datos,consulta):
        for i in consulta:
            if i['id_asesoria']==datos:
                return False
        return True

    
    def nuevoAviso(self,asunto,descripcion):
        filtro={}
        Mensajes={"De":"Admin","Asunto":asunto,"Descripcion":descripcion}
        nuevoVal={'$push':{'Avisos':Mensajes}}
        actuali=self.ActualizarDocuments("Usuarios",filtro,nuevoVal)
        return actuali
        

    def nuevaAsesoria(self):
        print()

    def nuevoComentario(self):
        print()

    
    def nuevoEvaluacion(self):
        print()

""" obj = MongoOnline()
datos={
            "nombre_usuario":"Karla Sambrano Perez",
            "correo":"KarlaSP19@gmail.com",
            "rol":"Estudiante",
            "clave":"123ksp",
        }
obj.conexion_mongoOnline()
obj.nuevoUsuario(datos)
obj.desconexion_mongoOnline() """



""" datos={
            "nombre_usuario":"Rafael Campos Salas",
            "correo":"Rafacs19@gmail.com",
            "rol":"Admin",
            "clave":"123cs",
        } """
""" obj.conexion_mongoOnline()
print(obj.encryptar('123jo'))
obj.desconexion_mongoOnline() """

""" obj = MongoOnline()
123Mqto 123Fta 123
datos={
"id_usuario":"us01",
"id_asesoria":"as04",
"nombre_asesoria":"Inteligencia Artificial"
    }
obj.conexion_mongoOnline()
print(obj.AsignarAsesoria(datos))
obj.desconexion_mongoOnline() """
#obj.datos_Asesoria_card()
#print(obj.secciones_Asesoria())



