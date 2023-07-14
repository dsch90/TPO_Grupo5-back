import model.usuario_model as modelo 
import controller.reserva_controller as reserva

class UsuarioController:

    def registro(self):

        print("Ok, vamos a registrarte en el sistema")

        nombre = input("¿Cual es tu nombre?:")
        correo = input("¿Cual es tu correo?: ")
        contacto = input("¿Cual es tu contacto?: ")
        direccion = input("¿Cual es tu direccion?: ")
        password = input("¿Cual es tu contraseña?: ")

        usuario = modelo.Usuario(nombre, correo, contacto, direccion, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado")

        else: 
            print("\nNo te has registrado correctamente!!!")

    def login(self):
        print("\nLogueate!!!")

        try:
            nombre_usuario = input("nombre de usuario: ")
            password_usuario = input("contraseña de usuario: ")

            usuario = modelo.Usuario(nombre_usuario,' ',' ',' ', password_usuario)
            login = usuario.identificar()

            if nombre_usuario == login[1]:
                print(f"\nBienvenido {login[1]}, te has identificado")
                self.proximasAcciones(login)
        except Exception as e:
            print(type (e))
            print(type(e).__name__)
            print(f"El login es incorrecto")


    def proximasAcciones(self, usuario):
        print("""Acciones disponibles:
              -crear
              -mostrar
              -eliminar
              -salir
              """)
        accion = input("elige una:")
        hazEl = reserva.ReservaController()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        