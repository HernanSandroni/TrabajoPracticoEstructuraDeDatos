from servidor_correo import ServidorCorreo
from usuario import Usuario

def mostrar_menu_principal():
    print("\n=== CLIENTE DE CORREO – UNaB ===")
    print("1. Iniciar sesión como usuario")
    print("2. Crear usuario nuevo")
    print("3. Salir")

def mostrar_menu_usuario(usuario):
    print(f"\n=== Menú de {usuario.nombre} ===")
    print("1. Ver carpetas")
    print("2. Enviar mensaje")
    print("3. Buscar mensaje")
    print("4. Aplicar filtros automáticos")
    print("5. Ver mensajes urgentes (cola prioridad)")
    print("6. Enviar mensaje por red (BFS/DFS)")
    print("7. Cerrar sesión")

def main():
    servidor = ServidorCorreo()  
    usuarios = {}  

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            if nombre in usuarios:
                usuario = usuarios[nombre]
                print(f"Sesión iniciada como {nombre}.")
                
                # === MENÚ DEL USUARIO ===
                while True:
                    mostrar_menu_usuario(usuario)
                    op = input("Seleccione una opción: ")

                    if op == "1":
                        usuario.mostrar_carpetas()

                    elif op == "2":
                        remitente = nombre
                        destinatario = input("Destinatario: ")
                        asunto = input("Asunto: ")
                        cuerpo = input("Mensaje: ")
                        servidor.enviar_mensaje(remitente, destinatario, asunto, cuerpo)

                    elif op == "3":
                        criterio = input("Buscar por asunto o remitente: ")
                        usuario.buscar_mensajes(criterio)

                    elif op == "4":
                        usuario.aplicar_filtros()

                    elif op == "5":
                        usuario.ver_urgentes()

                    elif op == "6":
                        servidor.simular_envio_red(nombre)

                    elif op == "7":
                        print("Sesión cerrada.")
                        break
                    
                    else:
                        print("Opción inválida.")

            else:
                print("Usuario no encontrado.")

        elif opcion == "2":
            nombre = input("Nuevo nombre de usuario: ")
            if nombre in usuarios:
                print("Ese usuario ya existe.")
            else:
                usuarios[nombre] = Usuario(nombre)
                print("Usuario creado con éxito.")

        elif opcion == "3":
            print("Saliendo del sistema…")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
