import controller.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1] 

class Estado:
    def __init__(self, nombre):
        self.nombre = nombre
