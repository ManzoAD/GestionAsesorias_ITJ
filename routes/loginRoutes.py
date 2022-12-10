from flask import Blueprint,render_template,request,flash,redirect,url_for
import jwt
from db.mongoOnline import MongoOnline

#Definir el blueprint para clientes
login = Blueprint('login',__name__)

#Definir la ruta de categorias
@login.route('/login' ,methods=['GET','POST'])
def consultar_categorias():
    if request.method=='POST':
        values=request.form.to_dict()
        objMong= MongoOnline()
        datLg=objMong.validarLogin(values)
        if len(datLg)>0:
            return redirect('/asesorias')
        else:
            print("vacio")

        #datos = objMong.validarLogin()
    return render_template('login.html')