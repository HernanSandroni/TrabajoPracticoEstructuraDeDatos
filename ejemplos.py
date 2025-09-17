# Crear servidor y usuarios
servidor = ServidorCorreo("Servidor UNaB")
juan = Usuario("Juan", "juan@mail.com")
ana = Usuario("Ana", "ana@mail.com")

servidor.registrar_usuario(juan)
servidor.registrar_usuario(ana)

# Juan envía mensaje a Ana
juan.enviar_mensaje(servidor, "ana@mail.com", "Hola", "¿Cómo estás?")

# Ana revisa bandeja
print(ana.listar_mensajes())


#ejemplo:
['2025-09-17 14:35:12.345678 | juan@mail.com -> Hola']
