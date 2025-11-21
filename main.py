from servidor_correo import ServidorCorreo
from usuario import Usuario
from mensaje import Mensaje


def mostrar_menu_principal():
    print("\n=== CLIENTE DE CORREO – UNaB ===")
    print("1. Iniciar sesión como usuario")
    print("2. Crear usuario nuevo")
    print("3. Salir")


def mostrar_menu_usuario(usuario):
    print(f"\n=== Menú de {usuario.nombre} ===")
    print("1. Ver carpetas y mensajes")
    print("2. Enviar mensaje")
    print("3. Buscar mensaje")
    print("4. Aplicar filtros automáticos")
    print("5. Ver mensajes urgentes (cola de prioridad)")
    print("6. Simular envío por red (BFS/DFS)")
    print("7. Cerrar sesión")


def main():
    servidor = ServidorCorreo()
    usuarios = {}

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        # ============================
        # INICIAR SESIÓN
        # ============================
        if opcion == "1":
            nombre = input("Ingrese su nombre: ")

            if nombre not in usuarios:
                print("❌ Usuario no encontrado.")
                continue

            usuario = usuarios[nombre]
            print(f"✔ Sesión iniciada como {nombre}.")

            # ============================================
            # MENÚ DEL USUARIO
            # ============================================
            while True:
                mostrar_menu_usuario(usuario)
                op = input("Seleccione una opción: ")

                # ------------------------------
                # 1. VER CARPETAS
                # ------------------------------
                if op == "1":
                    usuario.mostrar_carpetas()

                # ------------------------------
                # 2. ENVIAR MENSAJE
                # ------------------------------
                elif op == "2":
                    remitente = usuario.nombre
                    destinatario = input("Destinatario: ")

                    if destinatario not in usuarios:
                        print("❌ El destinatario no existe.")
                        continue

                    asunto = input("Asunto: ")
                    cuerpo = input("Mensaje: ")

                    urgente_op = input("¿Es urgente? (s/n): ").lower()
                    urgente = urgente_op == "s"

                    # Crear objeto Mensaje
                    msg = Mensaje(remitente, destinatario, asunto, cuerpo, urgente)

                    # Enviar y entregar
                    servidor.enviar_mensaje(remitente, destinatario, asunto, cuerpo, urgente)

                    usuarios[destinatario].recibir_mensaje(msg)

                    print("📨 Mensaje enviado con éxito.")

                # ------------------------------
                # 3. BUSCAR MENSAJE
                # ------------------------------
                elif op == "3":
                    criterio = input("Buscar por asunto o remitente: ")
                    usuario.buscar_mensajes(criterio)

                # ------------------------------
                # 4. APLICAR FILTROS
                # ------------------------------
                elif op == "4":
                    usuario.aplicar_filtros()

                # ------------------------------
                # 5. URGENTES
                # ------------------------------
                elif op == "5":
                    usuario.ver_urgentes()

                # ------------------------------
                # 6. SIMULACIÓN DE RED BFS / DFS
                # ------------------------------
                elif op == "6":
                    print("\n--- Simulación por red ---")
                    print("1. BFS (Recorrido en anchura)")
                    print("2. DFS (Recorrido en profundidad)")
                    metodo = input("Seleccione método: ")

                    if metodo == "1":
                        servidor.simular_envio_red(usuario.nombre, metodo="BFS")
                    elif metodo == "2":
                        servidor.simular_envio_red(usuario.nombre, metodo="DFS")
                    else:
                        print("❌ Método inválido.")

                # ------------------------------
                # 7. CERRAR SESIÓN
                # ------------------------------
                elif op == "7":
                    print("🔒 Sesión cerrada.")
                    break

                else:
                    print("❌ Opción inválida.")

        # ============================
        # CREAR NUEVO USUARIO
        # ============================
        elif opcion == "2":
            nombre = input("Nuevo nombre de usuario: ")

            if nombre in usuarios:
                print("❌ Ese usuario ya existe.")
            else:
                nuevo = Usuario(nombre)
                usuarios[nombre] = nuevo
                servidor.registrar_usuario(nombre)
                print("✔ Usuario creado con éxito.")

        # ============================
        # SALIR DEL SISTEMA
        # ============================
        elif opcion == "3":
            print("👋 Saliendo del sistema…")
            break

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()


