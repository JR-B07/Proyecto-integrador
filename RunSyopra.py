#importacion del framework
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='SyopraBD'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)


#declaracion de ruta / http://localhost:5000 - tipo insert 

@app.route('/')
def logicap():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM materiales')
    conmateriales = CC.fetchall() 
    print (conmateriales)
    return render_template('index.html', Listamateriales=conmateriales)

    
def __init__(self) -> None:
    pass
                       
@app.route('/guardarMaterial', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Nombre = request.form['txtnombre']
        Categoria = request.form['txtcategoria']
        Cantidad = request.form['txtcantidad']
        Max = request.form['txtmax']
        Min = request.form['txtmin']
        print(Nombre, Categoria, Cantidad, Max, Min)

        # Conectar a la base de datos
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO material (nombre, categoria, cantidad, max, min) VALUES (%s, %s, %s, %s, %s)', (Nombre, Categoria,Cantidad,Max,Min))
        mysql.connection.commit()

    flash('El Material fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM materiales WHERE id = %s', (id,))
    mysql.connection.commit()
    flash('Se eliminó el registro')
    return redirect(url_for('index'))

@app.route('/editar/<string:id>')
def editar(id):
    cursorID = mysql.connection.cursor()
    cursorID.execute('SELECT * FROM materiales WHERE id = %s', (id,))
    consultaID = cursorID.fetchone()

    return render_template('Actualizarmaterial.html', materiales=consultaID)

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varNombre = request.form['txtnombre']
        varCategoria = request.form['txtcategoria']
        varCantidad = request.form['txtcantidad']
        varMax = request.form['txtmax']
        varMin = request.form['txtmin']

        cursorAct = mysql.connection.cursor()
        cursorAct.execute('UPDATE materiales SET Nombre = %s, Categoria = %s, Cantidad = %s, Max = %s, Min = %s WHERE id = %s', (varNombre, varCategoria, varCantidad, varMax, varMin, id))
        mysql.connection.commit()

        flash('Se actualizó el registro ' + varNombre)
    return redirect(url_for('index'))
//////////////////////////
#compra
/
#reservaciones 
/////
entrega
////////

@app.route('/')
def proveedor():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM proveedor')
    conproveedor = CC.fetchall() 
    print (conproveedor)
    return render_template('index.html', Listaproveedor=conproveedor)

@app.route('/guardarProveedor', methods=['POST'])
def guardarProveedor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        print(nombre)

        # Conectar a la base de datos
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO proveedor (id_proveedor) VALUES (%s)', (nombre))
        mysql.connection.commit()

    flash('el proveedor fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminarProveedor/<int:id_proveedor>')
def eliminarProveedor(id_proveedor):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM proveedor WHERE id_proveedor = %s', (id_proveedor,))
    mysql.connection.commit()
    flash('el proveedor fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/editarProveedor/<string:id_proveedor>')
def editarProveedor(id_proveedor):
    cursorID = mysql.connection.cursor()
    cursorID.execute('SELECT * FROM proveedor WHERE id_proveedor = %s', (id_proveedor,))
    consultaID = cursorID.fetchone()

    return render_template('ActualizarProveedor.html', proveedor=consultaID)

@app.route('/actualizarProveedor/<int:id_proveedor>', methods=['POST'])
def actualizarProveedor(id_proveedor):
    if request.method == 'POST':
        proveedor = request.form['nombre']
        
        cursorAct = mysql.connection.cursor()
        cursorAct.execute('UPDATE nombre = %s  WHERE id_proveedor = %s', (proveedor, id_proveedor))
        mysql.connection.commit()

    flash('Se actualizó el registro ' + proveedor)
    return redirect(url_for('index'))
#ejecucion
if __name__ == '__main__':
    app.run(port= 5000)