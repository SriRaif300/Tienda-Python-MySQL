from AdminMenu import ObtenerValor
from Usuario import usuario
from Producto import producto
from Factura import factura

def ActualizarUsuario(usuarioActual):
    salir = True
    print("Tus datos actuales son: ")
    print("Nombre: " + usuarioActual.Getnombre())
    print("Apellido: "+ usuarioActual.Getapellido())
    print("Usuario: "+ usuarioActual.Getusuario() + "\n")

    usuarioActual.Setnombre(ObtenerValor("Ingresa tu nuevo nombre: "))
    usuarioActual.Setapellido(ObtenerValor("Ingresa tu nuevo apellido: "))
    usuarioActual.Setusuario(ObtenerValor("Ingresa tu nuevo usuario: "))
    usuarioActual.Setcontrasena(ObtenerValor("Ingresa tu nueva contraseña: "))

    while(salir):
        resultado = usuario.UsuarioExiste(usuario,usuarioActual.Getusuario())
        if len(resultado) == 0:
            usuarioActual.ActualizarDatos(usuarioActual.Getid())
            print("\nDatos Modificados\n")
            print("Tus Nuevos datos son: ")
            print("Nombre: " + usuarioActual.Getnombre())
            print("Apellido: "+ usuarioActual.Getapellido())
            print("Usuario: "+ usuarioActual.Getusuario() + "\n")
            salir = False
        else:
            print("\nEl usuario ya existe o esta vacio\n")
            usuarioActual.Setusuario(ObtenerValor("Ingresa tu nuevo usuario: "))

def CrearUsuarios():
    salir = True
    nombre = ObtenerValor("Ingresa tu nombre: ")
    apellido = ObtenerValor("Ingresa tu apellido: ")
    user = ObtenerValor("Ingresa tu usuario: ")
    contrasena = ObtenerValor("Ingresa tu contraseña: ")

    while(salir):
        resultado = usuario.UsuarioExiste(usuario,user)
        if len(resultado) == 0:
            nuevoUsuario = usuario(nombre,apellido,user,contrasena)
            nuevoUsuario.CrearUsuarios(0)
            print("\nUsuario Registrado con exito \nInicia sesion")
            usuarioActu = usuario.Login(usuario)
            salir = False
            return usuarioActu
        else:
            print("\nEl usuario ya existe\n")
            user = ObtenerValor("Ingrese otro Usuario: ")

def Comprar(usuarioActual):
    precioTotal = 0
    productosComprados = []
    salir = True
    while(salir):
        print("Lista de Productos\n")
        producto.EscribirProductos(producto)
        productosComprados.append(ObtenerValor("Ingrese el nombre de los productos que desea comprar: "))
        select = ObtenerValor("Quieres Segir comprando (S/N): ").lower()
        if select == "n":
            for articulo in productosComprados:
                    productoActual = producto.SaveProducto(producto,articulo)
                    if productoActual == None:
                        print(articulo,"no encontrado.")
                    else:
                        factura.CrearFactura(factura, usuarioActual.Getid(), productoActual)
                        precioTotal += productoActual.GetPrecio()
            print("Compra reailsada Coste total:",precioTotal,"€")
            salir = False
        elif select == "s":
            print("Producto agragado al carrito\n")
        else:
            print("Opcion Erronea")
            print("Porducto no agragado al carrito\n")
    
def MenuUsuario(usuarioActual):
    salir=True
    while salir:
        print("Que quires hacer: ")
        print("1. Ver productos \n2. Comprar productos \n3. Modificar sus datos \n4. Salir")
        select = input("Selecione una opcion: ")
        match select:
            case '1':
                print("Lista de Productos")
                producto.EscribirProductos(producto)
                print("\n")
            case '2':
                Comprar(usuarioActual)
            case '3':
                ActualizarUsuario(usuarioActual)
            case '4':
                salir=False
                print("\nAdios\n")
            case _:
                print("No has Selecionado nada \n")