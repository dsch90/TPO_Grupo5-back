import controller.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1] 

class Marca:
    def __init__(self, nombre):
        self.nombre = nombre

