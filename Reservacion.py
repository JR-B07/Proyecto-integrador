

@app.route('/')
def index():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM reservacion_de_materiales')
    conreservacion = CC.fetchall() 
    print (conreservacion)
    return render_template('index.html', Listareservacion=conreservacion)

@app.route('/ReservarMaterial', methods=['POST'])
def guardarReservacion():
    if request.method == 'POST':
        materialId = request.form['materialId']
        cantidadSolictud = request.form['cantidad']
        solicitante = request.form['solicitanteId']
        estado = request.form['estado']
        fecha = request.form['fecha']
        print(materialId,cantidadSolictud,solicitante,estado,fecha)

        # Conectar a la base de datos
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO reservacion_de_materiales (materialId, cantidad, solicitante, estado, fechas) VALUES (%s, %s, %s, %s, %s)', (materialId,cantidadSolictud,solicitante,estado,fecha))
        mysql.connection.commit()

    flash('la reservacion fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminarReservacion/<int:id_reservacion>')
def eliminarReservacion(id_reservacion):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM reservacion_de_materiales WHERE id_reservacion = %s', (id_reservacion,))
    mysql.connection.commit()
    flash('Se eliminó la reservacion')
    return redirect(url_for('index'))

@app.route('/editarReservacion/<string:id_reservacion>')
def editarReservacion(id_reservacion):
    cursorID = mysql.connection.cursor()
    cursorID.execute('SELECT * FROM reservacion_de_materiales WHERE id_reservacion = %s', (id_reservacion,))
    consultaID = cursorID.fetchone()

    return render_template('ActualizarReservacion.html', reservacion_de_materiales=consultaID)

@app.route('/actualizarReservacion/<int:id_compra>', methods=['POST'])
def actualizarReservacion(id_compra):
    if request.method == 'POST':
        idmaterial = request.form['id_material']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        idproveedor = request.form['id_proveedor']
        estadocompra = request.form['estado_compra']
        fecha = request.form['fecha']
        
        cursorAct = mysql.connection.cursor()
        cursorAct.execute('UPDATE compra_de_materiales SET id_material = %s, cantidad = %s, precio= %s, id_proveedor = %s, estado_compra = %s, fecha = %s WHERE id_compra = %s', (idmaterial,cantidad, precio, idproveedor,estadocompra,fecha, id_compra))
        mysql.connection.commit()

    flash('Se actualizó el registro ' + idmaterial)
    return redirect(url_for('index'))
