import mysql.connector

def EjecutarConsultaSQL(query, params=None):
    
    cnx = mysql.connector.connect(user='root', password='', host='localhost',database='tienda')
    cursor = cnx.cursor()
    
    cursor.execute(query, params)
    #Detecta si la consulta tiene algun valor
    if cursor.with_rows:
        #guarda el valor de la consulta en una varibale 
        resultado = cursor.fetchall()
    else:
        resultado = None

    cnx.commit()
    cursor.close()
    cnx.close()
    return resultado
    
def CrearTablas():
    sqlTableUser = """CREATE TABLE IF NOT EXISTS usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    usuario VARCHAR(255),
    contrasena VARCHAR(255),
    isAdmin BIT
    );"""
    EjecutarConsultaSQL(sqlTableUser)

    sqlTableProducto = """CREATE TABLE IF NOT EXISTS productos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255),
    precio FLOAT
    );"""
    EjecutarConsultaSQL(sqlTableProducto)

    sqlTableFactura = """CREATE TABLE IF NOT EXISTS facturas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario VARCHAR(255),
    producto VARCHAR(255),
    precio FLOAT
    );"""
    EjecutarConsultaSQL(sqlTableFactura)
