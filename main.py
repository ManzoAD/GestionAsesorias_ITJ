#import sys
from flask_cors import CORS
#sys.path.append(r'\Programas\ProgramasPhyton\Project')
from flask import Flask
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
CORS(app)

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


if __name__ == '__main__':
    #app = create_app()
    app.run()
    #serve(app, host='0.0.0.0', port=8000)