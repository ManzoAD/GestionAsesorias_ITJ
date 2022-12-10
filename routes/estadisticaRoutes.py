from flask import Blueprint,render_template


#Definir el blueprint para clientes
estadistica = Blueprint('estadistica',__name__)

#Definir la ruta de categorias
@estadistica.route('/estadistica')
def consultar_estadistica():
    return render_template('prueba.html')