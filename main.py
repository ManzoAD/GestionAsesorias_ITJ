#import sys
from flask_cors import CORS,cross_origin
import traceback
import predict_petal_length_controller
#sys.path.append(r'\Programas\ProgramasPhyton\Project')
from flask import Flask,request
import json
from flask_login import LoginManager
from db.models import UserModel
from waitress import serve

#from src import create_app
loginMan = LoginManager()

@loginMan.user_loader
def load_user(mail_login):
        print("esto llega",mail_login)
        return UserModel.query(mail_login)
        
#def create_app():
app = Flask(__name__)
# Configurar las referencias cruzadas, cuando se hacen peticiones de otros dominios
#CORS(app)
cors= CORS(app,resources={r"/predict_petal_lenght":{"origins":"*"}})
# Agregar configuración desde archivo configuracion.txt
app.config.from_object('configuracion.DevConfig')

#Registramos el login Manager
loginMan.init_app(app)
# Registramos los Blueprints
from routes.asesoriasRoutes import asesoria
app.register_blueprint(asesoria)

from routes.idxRoutes import indx
app.register_blueprint(indx)

from routes.estadisticaRoutes import estadistica
app.register_blueprint(estadistica)

from routes.loginRoutes import login
app.register_blueprint(login)

loginMan.login_view='login.consultar_categorias'
loginMan.login_message = u"Debes Iniciar Sesion Para Ingresar !!!"

from routes.registarRoutes import registro
app.register_blueprint(registro)

from routes.misasesoriasRoutes import misAseso
app.register_blueprint(misAseso)

@app.route('/predict_petal_lenght',methods=["GET"])
@cross_origin(origin="*",headers=['Content-Type'])
def predict_petal_lenght():
    try:
        petal_width = request.args.get('petal_width')
        lst= predict_petal_length_controller.function_predict(petal_width)
        resp= json.dumps(lst[0])
        return resp
    except Exception:
        return traceback.format_exc()

if __name__ == '__main__':
    #app = create_app()
    
    serve(app, host='0.0.0.0', port=8000)