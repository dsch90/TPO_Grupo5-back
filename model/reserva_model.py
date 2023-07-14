import datetime
import controller.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Reserva:
    def __init__(self, horario_salida_reserva, horario_regreso_reserva, usuario_reserva, estado_reserva, vehiculo_reserva):
        
        self.horario_salida_reserva = horario_salida_reserva
        self.horario_regreso_reserva = horario_regreso_reserva
        self.usuario_reserva = usuario_reserva
        self.estado_reserva = estado_reserva
        self.vehiculo_reserva = vehiculo_reserva

    def guardar(self):
        fecha = datetime.datetime.now()
        
        sql= "INSERT INTO reserva VALUES(null,%s,%s,%s,%s,%s,%s)"
        reserva = (fecha, self.horario_salida_reserva,self.horario_regreso_reserva,self.usuario_reserva,self.estado_reserva,self.vehiculo_reserva)


        try:
            cursor.execute(sql, reserva)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result