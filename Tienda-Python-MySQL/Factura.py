from SQLConsultas import EjecutarConsultaSQL

class factura:
    def __init__(self, usuario, producto, precio):
        self.__usuario = usuario
        self.__producto = producto
        self.__precio = precio

    def CrearFactura(self, user, Producto):
        productoId = Producto.GetId()
        precioProducto = Producto.GetPrecio()
        facturaNueva = factura(user, productoId, precioProducto)
        sql = "INSERT INTO facturas (usuario, producto, precio) VALUES (%s,%s,%s)"
        values = (facturaNueva.__usuario, facturaNueva.__producto, facturaNueva.__precio)
        EjecutarConsultaSQL(sql, values)

    def GetFacturaProducto(self, idPorducto):
        sql = "SELECT precio FROM facturas WHERE producto = %s"
        return EjecutarConsultaSQL(sql, (idPorducto,))
    
    def GetFacturaUsuario(self, idUsuario):
        sql = "SELECT precio FROM facturas WHERE usuario = %s"
        return EjecutarConsultaSQL(sql, (idUsuario,))
    
    def GetFactutara(self):
        sql = "SELECT precio FROM facturas"
        return EjecutarConsultaSQL(sql)

