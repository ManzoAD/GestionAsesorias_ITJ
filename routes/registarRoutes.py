from flask import Blueprint,render_template,request
from flask_login import login_required
import json
from ast import literal_eval as lte


#Definir el blueprint para clientes
registro = Blueprint('registro',__name__)

#Definir la ruta de categorias
@registro.route('/registrar',methods =['GET'])
@login_required
def consultar_categorias():
    
    if request.method == 'GET':
        search = request.values.to_dict()
        midict=lte(search['datos'])
    return render_template("registrar.html",datos=midict)

@registro.route('/registrar/asesoria',methods=['Get'])
def alumno_asesoria():
    print()