from flask import Flask
from flask_cors import CORS

# from src.categorias.routes import categoria

def create_app():
    app = Flask(__name__)
    # Configurar las referencias cruzadas, cuando se hacen peticiones de otros dominios
    CORS(app)
    # Agregar configuración desde archivo configuracion.txt
    app.config.from_object('configuracion.DevConfig')

    # Registramos los Blueprints
    from .routes.asesoriasRoutes import asesoria
    app.register_blueprint(asesoria)

    from .routes.idxRoutes import indx
    app.register_blueprint(indx)

    from .routes.estadisticaRoutes import estadistica
    app.register_blueprint(estadistica)

    from .routes.loginRoutes import login
    app.register_blueprint(login)
    return app