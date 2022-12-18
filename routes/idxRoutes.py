from flask import Blueprint,redirect,render_template


#Definir el blueprint para clientes
indx = Blueprint('indx',__name__)

#Definir la ruta de categorias
@indx.route('/')
def consultar_categorias():
    return render_template('index.html')

@indx.route('/LogOut')
def salida():
    return redirect('/')