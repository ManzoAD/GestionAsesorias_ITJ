from flask import Blueprint,render_template,session
from flask_login import login_required
from db.mongoOnline import MongoOnline
#Definir el blueprint para clientes
misAseso = Blueprint('misAseso',__name__)

#Definir la ruta de categorias
@misAseso.route('/misAsesorias')
@login_required
def consultar_estadistica():
    objMong= MongoOnline()
    objMong.conexion_mongoOnline()
    objMong.desconexion_mongoOnline()
    if session['rol']=="Estudiante":
        
        return render_template('asesorias.html')

    elif session['rol']=="Docente":
        return render_template('docente.html')

    elif session['rol']=="Admin":
        pass

    return render_template('admin.html')