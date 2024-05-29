
from  flask import Flask, render_template, request, redirect, url_for
import os
import database as db
#*===========================^^IMPORTACIONES^^==================================================
#! Configuración del directorio de plantillas
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')
#!===========================================================================
#? Creación de la aplicación Flask
app = Flask(__name__, template_folder=template_dir)
#?====================================================================================

#* Rutas de la aplicación

#? Ruta principal VIEWDATA
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute('SELECT * FROM clientes')
    myresult = cursor.fetchall()
    # Convertir los datos a un diccionario
    insertObject =[]
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close
    return render_template('viewdata.html', data=insertObject)
#?====================================================================================
#? RUTA BUSQUEDA DE USUARIO
@app.route('/buscar', methods=['POST'])
def search():
    cursor = db.database.cursor()   #? Conexion del cursor
    consulta = 'SELECT * FROM clientes WHERE serie LIKE %s ' #? consulta SQL
    serie = request.form['serie'] #? solicitar del formulario la busqueda
    cursor.execute(consulta, (f'%{serie}%',))    #? se executa la consulta del cursor en el valor recibido
    insertObject = [] #?lista vacia
    fila = cursor.fetchall() #? Recupero la fila donde haya coincidencia
    columnNames = [column[0] for column in cursor.description]
    for record in fila:
        insertObject.append(dict(zip(columnNames,record)))
    cursor.close() #? Cierro el cursor
    return render_template('search.html', consulta=insertObject)
#?=====================================================================================

#? TEMPLATE PAGINAS REDIRECCIONAMIENTO

@app.route('/addrepairpage')
def addrepair():
    return render_template('addrepair.html')

@app.route('/addpageclient')
def addpage():
    return render_template('addclient.html')

#?===========================================================================================================================================
            #TODO BOTONES REDIRECCIONAMIENTO
@app.route('/btnAddclient')
def buttonAddclient():
    return redirect(url_for('addpage'))

@app.route('/btnaddrepair')
def buttonaddrepair():
    return redirect(url_for('addrepair'))

@app.route('/btnHome')
def buttonHome():
    return redirect(url_for('home'))

#TODO==================================================================================================================================


#* Ruta para agregar usuarios

@app.route('/clientes', methods=['POST'])
def agregarUsuario():
    #? Obtener los datos del formulario
    name = request.form['name']
    lastname = request.form['lastname']
    rut = request.form['rut']
    brand = request.form['brand']
    model = request.form['model']
    serie = request.form['serie']
    #? Validar que los campos no estan vacios
    if name and lastname and rut and brand and model and serie:
        cursor = db.database.cursor()

        #? Consulta SQL para insertar nuevos usuarios
        sql = 'INSERT INTO clientes (nombre,apellido,rut,modelo,marca,serie) VALUES (%s,%s,%s,%s,%s,%s)'
        data = (name,lastname,rut,brand,model,serie)
        cursor.execute(sql, data)
        db.database.commit()
    
    return redirect(url_for('home'))
#*================================================================================================

#!Ruta para eliminar un usuario por su ID
## @app.route('/delete/<string:id>')
## def delete(id):
##     cursor = db.database.cursor()
##     # Consulta SQL para eliminar un usuario por su ID
##     sql = 'DELETE FROM clientes WHERE id=%s'
##     data = (id,)
##     cursor.execute(sql, data)
##     db.database.commit()
##     return redirect(url_for('home'))

#!Ruta para editar los datos de un usuario por su ID
@app.route('/editar/<string:serie>', methods=['GET', 'POST'])
def editar(serie):
    cursor = db.database.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE serie = %s", (serie,))
    data = cursor.fetchone()
    cursor.close()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        rut = request.form['rut']
        marca = request.form['marca']
        modelo = request.form['modelo']
        nserie = request.form['serie']
        cursor = db.database.cursor()
        cursor.execute("UPDATE clientes SET nombre = %s , apellido = %s , rut = %s, marca = %s , modelo= %s ,serie = %s WHERE serie = %s", (nombre, apellido, rut, marca, modelo, nserie, serie))
        db.database.commit()
        cursor.close()
        return 'Datos actualizados exitosamente!'
    return render_template('viewdata.html', data=data)

#* Si este script se ejecuta directamente, se inicia la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, port=4000)
