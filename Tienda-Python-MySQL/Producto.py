from SQLConsultas import EjecutarConsultaSQL

class producto:
    def __init__(self, nombre, precio, id=None):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio

    def CrearProductos(self):
        sql = "INSERT INTO productos (nombre, precio) VALUES (%s, %s)"
        values = (self.__nombre, self.__precio)
        EjecutarConsultaSQL(sql, values)
    
    def ActualizarProductos(self, nombreNuevo, precion, idProducto):
        sql="UPDATE productos SET nombre=%s, precio=%s WHERE id=%s"
        EjecutarConsultaSQL(sql, (nombreNuevo,precion,idProducto))

    def EscribirProductos(self):
        sql ="SELECT * FROM productos"
        for (id, nombre, precio) in EjecutarConsultaSQL(sql):
            print(id, nombre, precio, "€")

    def SaveProducto(self, name):
        sql = "SELECT * FROM productos WHERE nombre = %s"
        resultado = EjecutarConsultaSQL(sql,(name,)) 

        if len(resultado) == 0:
            return None

        id = resultado[0][0]
        nombre = resultado[0][1]
        precio = resultado[0][2]
        Producto = producto(nombre, precio, id)
        return Producto

    def GetId(self):
        return self.__id

    def GetNombre(self):
        return self.__nombre
    
    def SetNombre(self, value):
        self.__nombre = value

    def GetPrecio(self):
        return self.__precio
    
    def SetPrecio(self, value):
        self.__precio = value
    
    