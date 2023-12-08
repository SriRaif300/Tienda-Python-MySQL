from Usuario import usuario
from AdminMenu import MenuAdmin
from SQLConsultas import CrearTablas
from UsuarioMenu import CrearUsuarios
from UsuarioMenu import MenuUsuario

def CrearUsuarioAdmin():
    admin = usuario("admin","admin","admin","admin")
    admin.CrearUsuarios(1)

def MenuInicio():
    salir=True
    while salir:
        print("Bievenido a la tienda \nQue desea hacer")
        print("1. Registrase \n2. Iniciar Sesion \n3. Salir")
        select = input("Selecione una opcion: ")
        match select:
            case '1':
                usuarioActual = CrearUsuarios()
                return usuarioActual
            case '2':
                usuarioActual = usuario.Login(usuario)
                if usuarioActual == None:
                    usuarioActual = usuario.Login(usuario)
                else: 
                    return usuarioActual
            case '3':
                salir=False
                print("\nAdios\n")
            case _:
                print("No has Selecionado nada \n")

def main():
    CrearTablas()
    resultado = usuario.UsuarioExiste(usuario, "admin")
    if len(resultado) == 0:
        CrearUsuarioAdmin()
    
    usuarioActual = MenuInicio()
    if usuarioActual != None:
        if(usuarioActual.GetisAdmin() == 1):
            MenuAdmin()
        else:
            MenuUsuario(usuarioActual)

main()