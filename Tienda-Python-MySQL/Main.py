from Usuario import usuario
from AdminMenu import MenuAdmin
from SQLConsultas import CrearTablas
from UsuarioMenu import CrearUsuarios
from UsuarioMenu import MenuUsuario

def CrearUsuarioAdmin():
    admin = usuario("admin","admin","admin","8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918")
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
                salir = False
                return usuarioActual
            case '3':
                salir=False
                print("\nAdios\n")
            case _:
                print("No has selecionado nada \n")

def main():
    CrearTablas()
    resultado = usuario.UsuarioAdminExiste(usuario, 1)
    if len(resultado) == 0:
        CrearUsuarioAdmin()

    usuarioActual = MenuInicio()
    while True:
        if usuarioActual != None:
            if(usuarioActual.GetisAdmin() == 1):
                MenuAdmin(usuarioActual)
                return
            else:
                MenuUsuario(usuarioActual)
                return
        else:
            usuarioActual = MenuInicio()

main()