from flask import Blueprint


#Definir el blueprint para clientes
indx = Blueprint('indx',__name__)

#Definir la ruta de categorias
@indx.route('/')
def consultar_categorias():
    return"Bienvenido a Index......."