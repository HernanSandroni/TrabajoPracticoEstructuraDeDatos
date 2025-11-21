from servidor_correo import ServidorCorreo
from usuario import Usuario
from mensaje import Mensaje

# ============================
# MENÚ PRINCIPAL
# ============================
def mostrar_menu_principal():
    print("\n=== CLIENTE DE CORREO – UNaB ===")
    print("1. Iniciar sesión como usuario")
    print("2. Crear usuario nuevo")
    print("3. Salir")

# ============================
# MENÚ DE USUARIO
# ============================
def mostrar_menu_usuario(usuario):
    print(f"\n=== Menú de {usuario.nombre} ===")
    print("1. Ver carpetas y mensajes")
    print("2. Enviar mensaje")
    print("3. Buscar mensaje")
    print("4. Aplicar filtros automáticos")
    print("5. Ver mensajes urgentes (cola de prioridad)")
    print("6. Mover mensaje entre carpetas")
    print("7. Simular envío por red (BFS/DFS)")
    print("8. Cerrar sesión")

# ============================
# MAIN
# ============================
def main():
    servidor = ServidorCorreo()
    usuarios = {}

    # Crear servidores de ejemplo para la red
    servidor.agregar_conexion("Servidor1", "Servidor2")
    servidor.agregar_conexion("Servidor2", "Servidor3")
    servidor.agregar_conexion("Servidor3", "Servidor4")

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        # --------------------------
        # 1. INICIAR SESIÓN
        # --------------------------
        if opcion == "1":
            nombre = input("Ingrese su nombre: ")

            if nombre not in usuarios:
                print("❌ Usuario no encontrado.")
                continue

            usuario = usuarios[nombre]
            print(f"✔ Sesión iniciada como {nombre}.")

            while True:
                mostrar_menu_usuario(usuario)
                op = input("Seleccione una opción: ")

                # ------------------------------
                # 1. Ver carpetas
                # ------------------------------
                if op == "1":
                    usuario.mostrar_carpetas()

                # ------------------------------
                # 2. Enviar mensaje
                # ------------------------------
                elif op == "2":
                    destinatario = input("Destinatario: ")
                    if destinatario not in usuarios:
                        print("❌ El destinatario no existe.")
                        continue

                    asunto = input("Asunto: ")
                    cuerpo = input("Mensaje: ")
                    urgente = input("¿Es urgente? (s/n): ").lower() == "s"

                    # Se envía usando solo ServidorCorreo
                    servidor.enviar_mensaje(usuario.nombre, destinatario, asunto, cuerpo, urgente)

                # ------------------------------
                # 3. Buscar mensaje
                # ------------------------------
                elif op == "3":
                    criterio = input("Buscar por asunto o remitente: ")
                    usuario.buscar_mensajes(criterio)

                # ------------------------------
                # 4. Aplicar filtros
                # ------------------------------
                elif op == "4":
                    usuario.aplicar_filtros()

                # ------------------------------
                # 5. Ver mensajes urgentes
                # ------------------------------
                elif op == "5":
                    usuario.ver_urgentes()

                # ------------------------------
                # 6. Mover mensaje entre carpetas
                # ------------------------------
                elif op == "6":
                    print("\n--- Mover mensaje ---")
                    asunto = input("Ingrese el asunto del mensaje a mover: ")
                    carpeta_destino = input("Ingrese el nombre de la carpeta destino: ")

                    encontrados = usuario.carpetas.buscar_recursivo(asunto)
                    if not encontrados:
                        print("❌ No se encontró el mensaje.")
                    else:
                        mensaje = encontrados[0]
                        usuario.carpetas.mover_mensaje_recursivo(mensaje, carpeta_destino)
                        print(f"✔ Mensaje '{asunto}' movido a {carpeta_destino}")

                # ------------------------------
                # 7. Simular envío BFS/DFS
                # ------------------------------
                elif op == "7":
                    print("\n--- Simulación de envío por red ---")
                    print("Servidores disponibles:", list(servidor.red.keys()))
                    servidor_origen = input("Servidor origen: ")
                    metodo = input("Método (BFS/DFS): ").upper()
                    servidor.simular_envio_red(usuario.nombre, metodo=metodo, servidor_origen=servidor_origen)

                # ------------------------------
                # 8. Cerrar sesión
                # ------------------------------
                elif op == "8":
                    print("🔒 Sesión cerrada.")
                    break

                else:
                    print("❌ Opción inválida.")

        # --------------------------
        # 2. Crear usuario nuevo
        # --------------------------
        elif opcion == "2":
            nombre = input("Nuevo nombre de usuario: ")
            if nombre in usuarios:
                print("❌ Ese usuario ya existe.")
            else:
                nuevo = Usuario(nombre)
                usuarios[nombre] = nuevo
                servidor.registrar_usuario(nuevo)
                print("✔ Usuario creado con éxito.")

        # --------------------------
        # 3. Salir
        # --------------------------
        elif opcion == "3":
            print("👋 Saliendo del sistema…")
            break

        else:
            print("❌ Opción inválida.")


# ============================
# EJECUCIÓN PRINCIPAL
# ============================
if __name__ == "__main__":
    main()



