from SQLConsultas import EjecutarConsultaSQL
from hashlib import sha256
from getpass import getpass

class usuario:
    def __init__(self, nombre, apellido, usuario, contrasena, id=None, isAdmin=None):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__contrasena = contrasena
        self.__isAdmin = isAdmin

    def ObtenerValor(self, mensaje):
        valor = input(mensaje)
        while not valor:
            print("El valor no puede estar vacío.")
            valor = input(mensaje)
        return valor
    
    def ObtenerValor_Pasword(self, mensaje):
        valor = getpass(mensaje)
        while not valor:
            print("El valor no puede estar vacío.")
            valor = input(mensaje)
        return valor
    
    def SaveUser(self, idUsuario):
        sql = "SELECT * FROM usuarios WHERE id = %s"
        resultado =  EjecutarConsultaSQL(sql, (idUsuario,))

        id = resultado[0][0]
        nombre = resultado[0][1]
        apellido = resultado[0][2]
        nombreUsuario = resultado[0][3]
        contrasena = resultado[0][4]
        isAdmin = resultado[0][5]
        user = usuario(nombre, apellido, nombreUsuario, contrasena, id, isAdmin)
        return user
    
    def Login(self):
        Usuario = self.ObtenerValor(self,"Dime tu usuario: ")
        contrasena = self.ObtenerValor_Pasword(self,"Dime tu Contraseña: ")
        contrasena = sha256(contrasena.encode('utf-8')).hexdigest()
        sql = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s"
        values = (Usuario, contrasena)
        resultado = EjecutarConsultaSQL(sql, values)
        if len(resultado) == 0:
            print("\nUsuario o contraseña no son correctos\n")
            return None
        else:
            print("\nBienvenido\n")
            usuarioActual = self.SaveUser(usuario,resultado[0][0])
            return usuarioActual

    def BorrarUsuario(self, idUsuario):
        sql="DELETE FROM usuarios WHERE id = %s"
        EjecutarConsultaSQL(sql, (idUsuario,))

    def EscribirUsuarios(self):
        sql ="SELECT id, usuario FROM usuarios"
        for (id, user) in EjecutarConsultaSQL(sql):
            print(id, user) 

    def ActualizarDatos(self, idUsuario):
        sql = "UPDATE usuarios SET nombre = %s, apellido = %s, usuario = %s, contrasena = %s WHERE id = %s"
        values = (self.__nombre, self.__apellido, self.__usuario, self.__contrasena, idUsuario)
        EjecutarConsultaSQL(sql, values)
        self.SaveUser(idUsuario)

    def CrearUsuarios(self, admin):
        sql =("INSERT INTO usuarios (nombre, apellido, usuario, contrasena, isAdmin) VALUES (%s,%s,%s,%s,%s)")
        values = (self.__nombre, self.__apellido, self.__usuario, self.__contrasena, admin)
        EjecutarConsultaSQL(sql, values)

    def UsuarioExiste(self, Usuario):
        sql = "SELECT usuario FROM usuarios WHERE usuario = %s"
        return EjecutarConsultaSQL(sql,(Usuario,))
    
    def UsuarioAdminExiste(self, id):
        sql = "SELECT usuario FROM usuarios WHERE id = %s"
        return EjecutarConsultaSQL(sql,(id,))
    
    def Getid(self):
        return self.__id

    def Getnombre(self):
        return self.__nombre

    def Setnombre(self, value):
        self.__nombre = value
    
    def Getapellido(self):
        return self.__apellido

    def Setapellido(self, value):
        self.__apellido = value
    
    def Getusuario(self):
        return self.__usuario

    def Setusuario(self, value):
        self.__usuario = value

    def Getusuario(self):
        return self.__usuario

    def Setusuario(self, value):
        self.__usuario = value

    def Getcontrasena(self):
        return self.__contrasena

    def Setcontrasena(self, value):
        self.__contrasena = value

    def GetisAdmin(self):
        return self.__isAdmin

    def SetisAdmin(self, value):
        self.__isAdmin = value