from flask_login import UserMixin
from db.mongoOnline import MongoOnline
class UserData():
    def __init__(self,user_id,user_mail,user_password):
        self.user_id=user_id
        self.user_mail = user_mail
        self.user_password = user_password

class UserModel(UserMixin):
    def __init__(self,user_data):
        self.id = user_data.user_id
        self.mail = user_data.user_mail
        self.password = user_data.user_password
    
    @staticmethod
    def query(user_id):
        objM = MongoOnline()
        objM.conexion_mongoOnline()
        user_doc =objM.obtener_usuario(user_id)
        if user_doc:
            objM.desconexion_mongoOnline()
            user_data =UserData(
                user_id=user_doc[0]['id_usuario'],
                user_mail= user_doc[0]['correo'],
                user_password= user_doc[0]['clave']) 
            return UserModel(user_data)
        return None

