import pymongo
import bcrypt
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
        response =[]
        self.MONGO_RESPUESTA= self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].find(filtro,atributos)
        if self.MONGO_RESPUESTA:
            for reg in self.MONGO_RESPUESTA:
                response.append(reg)
        return response

#Actualizacion general de la asesoria
    def ActualizarDocuments(self,tabla,filtro,nuevos_valores):
        self.MONGO_RESPUESTA= self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].update_one(filtro,nuevos_valores)
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
        atribu={"_id":0,"id_usuario":1,"correo":1,"clave":1}
        filtro={"id_usuario":id_usuario}
        respuesta= self.consulta_mongodbOnline("Usuarios",filtro,atribu)
        if respuesta:
            return respuesta
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
        return contra_cifrada

    def AsignarAsesoria(self,datos):
        #debemos recibir el id_usuarios, id_asesoria, nombre_asesoria
        filtro={"id_usuario":datos['id_usuario'],"data_asesorias":[{'id_asesoria':datos['id_asesoria'],"nombre_asesoria":datos["nombre_asesoria"]}]}
        atributos={"_id":0,"data_asesorias":1,"nombre_usuario":1}
        consu =self.consulta_mongodbOnline("Usuarios",filtro,atributos)
        if  len(consu)==0: #No tiene registrada la asesoria, se actualiaza
            filtro={"id_usuario":datos['id_usuario']}
            consu=self.consulta_mongodbOnline("Usuarios",filtro,atributos)
            if len(consu[0]['data_asesorias'])==3:
                return "Error: Haz alcanzado el maximo de asesorias (3)"
            else:
                filtro={"id_usuario":datos['id_usuario']}
                nuevoVal={'$push':{'data_asesorias':
                {
                    "id_asesoria":datos['id_asesoria'],
                    "nombre_asesoria":datos["nombre_asesoria"]
                    }}}
                actual=self.ActualizarDocuments("Usuarios",filtro,nuevoVal)
                if actual:
                    return "Actualizacion Exitosa"
                else:
                    return "Error en Actualizacion"
        
        
        return "Error: La asesoria ya habia sido registrada"




    def nuevaAsesoria(self):
        print()

    def nuevoComentario(self):
        print()

    def nuevoAviso(self):
        print()
    
    def nuevoEvaluacion(self):
        print()

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
