import controller.conexion as conexion
import hashlib

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, nombre_usuario, correo_usuario, contacto_usuario, direccion_usuario, password_usuario):
        self.nombre_usuario = nombre_usuario
        self.correo_usuario = correo_usuario
        self.contacto_usuario = contacto_usuario
        self.direccion_usuario = direccion_usuario
        self.password_usuario = password_usuario
    

    def registrar(self):
        #cifrado = hashlib.sha256()
        #cifrado.update(self.password_usuario.encode('utf8'))  #me convierte el valor a byte

        sql= "INSERT INTO usuario VALUES(null,%s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.correo_usuario,self.contacto_usuario,self.direccion_usuario,self.password_usuario)


        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result
    
    def identificar(self):
        
        sql = "SELECT * FROM usuario WHERE nombre_usuario = %s AND password_usuario = %s"

        ##cifrado = hashlib.sha256()
        ##cifrado.update(self.password_usuario.encode('utf8'))  #me convierte el valor a byte
        
        
        usuario = (self.nombre_usuario, self.password_usuario)

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result

