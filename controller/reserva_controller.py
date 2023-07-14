import model.reserva_model as reserva

class ReservaController:

    def crear(self, usuario):
        print("Ok, vamos a crear una reserva en el sistema")
        horario_salida_reserva =  input("horario_salida_reserva")
        horario_regreso_reserva =  input("horario_regreso_reserva")
        estado_reserva =  input("estado_reserva") 
        vehiculo_reserva =  input("vehiculo_reserva")

        reserva_usuario = reserva.Reserva(horario_salida_reserva, horario_regreso_reserva, usuario[0], estado_reserva, vehiculo_reserva)
        reservacion = reserva_usuario.guardar()

        if reservacion[0] >= 1:
            print(f"\nPerfecto {reservacion[1].fecha_reserva} {reservacion[4].usuario_reserva}  se ha reservado")

        else: 
            print("\nNo se ha reservado!!!")
