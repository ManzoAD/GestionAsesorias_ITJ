from flask import Blueprint,render_template,request,flash,redirect,url_for,session
from flask_login import login_user
from db.mongoOnline import MongoOnline
from db.models import UserData, UserModel
import jwt

#Definir el blueprint para clientes
login = Blueprint('login',__name__)

#Definir la ruta de categorias
@login.route('/login' ,methods=['GET','POST'])
def consultar_categorias():
    if request.method=='POST':
        values=request.form.to_dict()
        objMong= MongoOnline()
        objMong.conexion_mongoOnline()
        datLg=objMong.validarLogin(values)
        objMong.desconexion_mongoOnline()
        print(datLg)
        secreto = "Palabra_Secreta"
        if datLg: #El usuario ha sido validado con exito
            token = jwt.encode({
            'id':datLg['id_usuario'],
            "correo":datLg['correo'],
            "rol":datLg['rol'],
            "clave":datLg["clave"]
            },
            secreto,
            algorithm="HS256"
            )
            session['token']=token
            session['rol']=datLg['rol']
            userdata=UserData(datLg['id_usuario'],datLg['correo'],datLg['clave'])
            user=UserModel(userdata)
            login_user(user)
            flash("Bienvenido",datLg['correo'])
            return redirect('/asesorias')
        else:
            flash("Login Incorrecto, Verifica tus credenciales")
    return render_template('login.html')