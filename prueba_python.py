from controller import usuario_controller
print("""
Acciones disponibles:
- registro
- login
""")

hazEl = usuario_controller.UsuarioController()
accion = input("que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
