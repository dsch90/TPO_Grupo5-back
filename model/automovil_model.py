import controller.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Automovil:
    def __init__(self, nombre_automovil, descripcion_automovil, precio_automovil, marca_automovil, categoria_automovil, estado_automovil):
        self.nombre_automovil = nombre_automovil
        self.descripcion_automovil = descripcion_automovil
        self.precio_automovil = precio_automovil
        self.marca_automovil = marca_automovil
        self.categoria_automovil = categoria_automovil
        self.estado_automovil = estado_automovil


