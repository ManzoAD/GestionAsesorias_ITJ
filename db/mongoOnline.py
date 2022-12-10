import pymongo
class MongoOnline:
    def __init__(self):
        self.MONGO_DATABASE = "Gestion_Asesorias"
        self.MONGO_URI = 'mongodb+srv://m4nz0diego386:LPG186mongo01@cluster0.hj6tahj.mongodb.net/?retryWrites=true&w=majority'
        self.MONGO_CLIENT =None
        self.MONGO_RESPUESTA= None
        self.MONGO_TIMEOUT=1000

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
        response ={"status":False,"resultado":[]}
        self.MONGO_RESPUESTA= self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].find(filtro,atributos)
        if self.MONGO_RESPUESTA:
            response["status"]=True
            for reg in self.MONGO_RESPUESTA:
                response['resultado'].append(reg)
        return response

#Consultas especificas
    def datos_Asesoria_card(self):
        self.conexion_mongoOnline()
        atribu={"_id":0,"nombre_asesoria":1,"docente":1,"horario":1,"Area":1,"Temario":1,"Espacios_disponibles":1}
        filtro={}
        respuesta= self.consulta_mongodbOnline("Asesorias",filtro,atribu)
        self.desconexion_mongoOnline()
        return respuesta['resultado']
    def datos_comentarios(self):
        self.conexion_mongoOnline()
        filtro={}
        respuesta= self.consulta_mongodbOnline("Comentarios",filtro)
        self.desconexion_mongoOnline()
        return respuesta['resultado']

    def insertar_Comentario(self,descrip="",idCom="c20",nomUsu="Diego Manzo",idUS="us01"):
        respuesta={}
        documento={
            "id_comentario":idCom,
            "descripcion":descrip,
            "reacciones":[],
            "c_usuario":[{"id_usuario":idUS,"nombre":nomUsu}]
        }
        self.conexion_mongoOnline()
        self.MONGO_RESPUESTA= self.MONGO_CLIENT[self.MONGO_DATABASE]["Comentarios"].insert_one(documento)
        if self.MONGO_RESPUESTA:
            respuesta["resultado"]="Comentario Ingresado con exito!!!"
            print("Valido")
        else:
            respuesta["resultado"]="Error comentario no ingresado!!!!"
            print("no valido")
        self.desconexion_mongoOnline()


    def secciones_Asesoria(self):
        secciones=[]
        self.conexion_mongoOnline()
        atribu={"_id":0,"Area":1}
        filtro={}
        respuesta= self.consulta_mongodbOnline("Asesorias",filtro,atribu)
        for i in respuesta['resultado']:
            if(i["Area"] not in secciones):
                secciones.append(i["Area"])
        self.desconexion_mongoOnline()
        return secciones
    
    def validarLogin(self,dtos):
        self.conexion_mongoOnline()
        filtro={"correo":dtos['mail_login'],"clave":dtos["clave_form"],"rol":dtos["RadioSesion"]}
        atributos={"_id":0,"id_usuario":1,"correo":1,"rol":1,"clave":1}
        valor= self.consulta_mongodbOnline("Usuarios",filtro,atributos)
        datos={}
        if len(valor["resultado"])>0:
            datos={
                "id_usuario":valor["resultado"][0]["id_usuario"],
                "correo":valor["resultado"][0]["correo"],
                "rol":valor["resultado"][0]["rol"],
                "clave":valor["resultado"][0]["clave"]
            }
        self.desconexion_mongoOnline()
        return datos

    
#Inserciones de los valores
    def nuevoUsuario(self):
        print()
    
    def nuevaAsesoria(self):
        print()

    def nuevoComentario(self):
        print()

    def nuevoAviso(self):
        print()
    
    def nuevoEvaluacion(self):
        print()

#obj = MongoOnline()
#obj.datos_Asesoria_card()
#print(obj.secciones_Asesoria())
