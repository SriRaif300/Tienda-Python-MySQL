from Usuario import usuario
from Producto import producto
from Factura import factura
from UsuarioMenu import ActualizarUsuario
from getpass import getpass

def ObtenerValor(mensaje):
    valor = input(mensaje)
    while not valor:
        print("El valor no puede estar vacío.")
        valor = input(mensaje)
    return valor

def ObtenerValor_Pasword(mensaje):
    valor = getpass(mensaje)
    while not valor:
        print("El valor no puede estar vacío.")
        valor = input(mensaje)
    return valor

def CrearProductos():
    nombre = ObtenerValor("Pon el nombre del producto: ") 
    precio = ObtenerValor("Pon el precio del producto: ")
    salir = True
    while(salir): 
        productoActual = producto.SaveProducto(producto, nombre)
        if productoActual == None:
            productoActual = producto(nombre, precio)
            productoActual.CrearProductos()
            print("\nProducto Creado\n")
            salir = False
        else:
            print("El nombre del producto ya existe")
            nombre = ObtenerValor("Pon el nombre del producto: ")

def ModificarProductos():
    print("Lista de Productos\n")
    producto.EscribirProductos(producto)
    idProducto = ObtenerValor("\nEscribe el numero del producto que quieres Modificar: ")
    
    nombreNuevo = ObtenerValor("Pon el nuevo nombre del producto: ")
    precio = ObtenerValor("Pon el nuevo precio del producto: ")
    salir = True
    while(salir): 
        productoActual = producto.SaveProducto(producto, nombreNuevo)
        if productoActual == None:
            producto.ActualizarProductos(producto, nombreNuevo, precio, idProducto)
            print("\nProducto Actualizado\n")
            salir = False
        else:
            print("El nombre del producto ya existe")
            nombreNuevo = ObtenerValor("Pon el nombre del producto: ")
    
def EliminarUsuarios():
    print("Lista de Usuarios\n")
    usuario.EscribirUsuarios(usuario)
    idUsuario = ObtenerValor("\nIngrese el numero del usuario que desea borrar: ")
    
    usuario.BorrarUsuario(usuario, idUsuario)
    print("\nUsuario Eliminado\n")
    
def CrearFacturaTotal():
    print("Factura Total: ")
    nuevaFactura = factura.GetFactutara(factura)
    productosTotales = len(nuevaFactura)
    precioTotal = 0
    for item in nuevaFactura:
        precioTotal += item[0]
    print("\nEl total de articulos comprados son:",productosTotales,"y las Ganasias son:",precioTotal,"€\n")

def CrearFacturaUsuario():
    salir = True
    while(salir):
        print("Lista de Usuarios")
        usuario.EscribirUsuarios(usuario)
        idUsuario = ObtenerValor("Escribe el numero del Usuario que le quieras sacar la factura (solo uno): ")
        usuarioFactura = usuario.UsuarioExiste(usuario, idUsuario)
        if usuarioFactura == None:
            print("EL Usuario no existe o lo has introducido Mal")
        else:
            usuarioNew = usuario.SaveUser(usuario, idUsuario)
            nuevaFactura = factura.GetFacturaUsuario(factura, idUsuario)
            productosTotales = len(nuevaFactura)
            precioTotal = 0
            for item in nuevaFactura:
                precioTotal += item[0]
            print("\nEl total de articulos comprados por", usuarioNew.Getusuario(), "son:",productosTotales,"y sus gastos son:",precioTotal,"€\n")
            salir=False

def CrearFacturaProducto():
    salir = True
    while(salir):
        print("Lista de Productos\n")
        producto.EscribirProductos(producto)

        nombreProducto = ObtenerValor("Escribe el nombre del producto que le quieras sacar la factura (solo uno): ")
        productoActual = producto.SaveProducto(producto, nombreProducto)
        if productoActual == None:
            print("EL producto no existe o lo has introducido Mal")
        else:
            nuevaFactura = factura.GetFacturaProducto(factura, productoActual.GetId())
            productosTotales = len(nuevaFactura)
            precioTotal = 0
            for item in nuevaFactura:
                precioTotal += item[0]
            print("\nEl total de", productoActual.GetNombre(), "comprad@s son:",productosTotales,"y sus ganacias son:",precioTotal,"€\n")
            salir=False

def MenuAdmin(usuarioActual):
    salir=True
    while salir:
        print("Bienvenido al panel de administrador \nQue quires hacer: ")
        print("1. Crear productos \n2. Modificar productos\n3. Modificar tus datos \n4. Eliminar Usuarios \n5. Sacar la Facturación total \n6. Sacar la Facturación por usuario \n7. Sacar la Facturación por producto \n8. Salir")
        select = input("Selecione una opcion: ")
        match select:
            case '1':
                CrearProductos()
            case '2':
                ModificarProductos()
            case '3':
                ActualizarUsuario(usuarioActual)
            case '4':
                EliminarUsuarios()
            case '5':
                CrearFacturaTotal()
            case '6':
                CrearFacturaUsuario()
            case '7':
                CrearFacturaProducto()
            case '8':
                print("\nAdios\n")
                salir=False
            case _:
                print('No has Selecionado nada\n')