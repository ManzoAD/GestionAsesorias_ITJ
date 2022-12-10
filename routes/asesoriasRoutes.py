from flask import Blueprint,render_template,request
from db.mongoOnline import MongoOnline

#Definir el blueprint para clientes
asesoria = Blueprint('asesoria',__name__)

#Definir la ruta de categorias
@asesoria.route('/asesorias')
def consultar_categorias():
    objMongo = MongoOnline()
    datAseso=objMongo.datos_Asesoria_card()
    datComment= objMongo.datos_comentarios()
    secciones =objMongo.secciones_Asesoria()
    return render_template('mobInicio.html',datos=datAseso,seccionar=secciones,comentar=datComment)

@asesoria.route('/asesorias/comentario',methods=['POST','GET'])
def ingresar_comentario():
    valores = request.form["comUs"]
    print(valores)
    objMongo = MongoOnline()
    objMongo.insertar_Comentario(valores)
    datAseso=objMongo.datos_Asesoria_card()
    datComment= objMongo.datos_comentarios()
    secciones =objMongo.secciones_Asesoria()
    return  render_template('mobInicio.html',datos=datAseso,seccionar=secciones,comentar=datComment)
    