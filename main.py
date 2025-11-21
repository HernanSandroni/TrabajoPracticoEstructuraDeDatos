from servidor_correo import ServidorCorreo
from usuario import Usuario
from mensaje import Mensaje


# ==============================
#   MENÚS Y OPCIONES
# ==============================

def mostrar_menu_principal():
    print("\n======= CLIENTE DE CORREO – UNaB =======")
    print("1. Iniciar sesión")
    print("2. Crear usuario nuevo")
    print("3. Salir")
    print("========================================")


def mostrar_menu_usuario(usuario):
    print(f"\n======= Sesión de {usuario.nombre} =======")
    print("1. Ver estructura de carpetas (árbol)")
    print("2. Enviar mensaje")
    print("3. Buscar mensaje (recursivo)")
    print("4. Aplicar filtros automáticos")
    print("5. Ver mensajes urgentes (cola prioridad)")
    print("6. Simular envío por red (BFS/DFS)")
    print("7. Ver bandeja de entrada")
    print("8. Cerrar sesión")
    print("==========================================")


# ==============================
#   PROGRAMA PRINCIPAL
# ==============================

def main():
    print("\n*** INICIANDO SISTEMA DE CORREO UNaB ***")

    servidor = ServidorCorreo()  # Grafo + red + envío
    usuarios = {}                # Almacenamiento en memoria

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()

        # ==============================
        # INICIAR SESIÓN
        # ==============================
        if opcion == "1":
            nombre = input("Nombre de usuario: ").strip()

            if nombre not in usuarios:
                print("❌ Usuario no encontrado.")
                continue

            usuario = usuarios[nombre]
            print(f"✔ Sesión iniciada como {nombre}")

            # MENÚ DEL USUARIO
            while True:
                mostrar_menu_usuario(usuario)
                op = input("Seleccione una opción: ").strip()

                # ==============================
                # VER CARPETAS
                # ==============================
                if op == "1":
                    print("\n--- ESTRUCTURA DE CARPETAS ---")
                    usuario.carpetas.mostrar_estructura()

                # ==============================
                # ENVIAR MENSAJE
                # ==============================
                elif op == "2":
                    destinatario = input("Destinatario: ")
                    asunto = input("Asunto: ")
                    cuerpo = input("Mensaje: ")

                    if destinatario not in usuarios:
                        print("❌ Ese usuario no existe.")
                        continue

                    msg = Mensaje(usuario.nombre, destinatario, asunto, cuerpo)

                    servidor.enviar_mensaje(usuario.nombre, destinatario, asunto, cuerpo)
                    usuarios[destinatario].recibir_mensaje(msg)

                    print("✔ Mensaje enviado correctamente.")

                # ==============================
                # BÚSQUEDA RECURSIVA
                # ==============================
                elif op == "3":
                    criterio = input("Buscar por asunto o remitente: ")
                    print("\n--- RESULTADOS DE BÚSQUEDA ---")
                    usuario.buscar_mensajes(criterio)

                # ==============================
                # APLICAR FILTROS AUTOMÁTICOS
                # ==============================
                elif op == "4":
                    print("\nAplicando filtros automáticos…")
                    usuario.aplicar_filtros()
                    print("✔ Mensajes ordenados según reglas.")

                # ==============================
                # COLA DE PRIORIDAD
                # ==============================
                elif op == "5":
                    print("\n--- MENSAJES URGENTES ---")
                    usuario.ver_urgentes()

                # ==============================
                # GRAFO + BFS/DFS
                # ==============================
                elif op == "6":
                    print("\n--- SIMULACIÓN DE RED DE SERVIDORES ---")
                    print("1. BFS")
                    print("2. DFS")
                    metodo = input("Método de recorrido: ")

                    if metodo == "1":
                        servidor.simular_envio_red(usuario.nombre, metodo="BFS")
                    elif metodo == "2":
                        servidor.simular_envio_red(usuario.nombre, metodo="DFS")
                    else:
                        print("❌ Método inválido.")

                # ==============================
                # VER BANDEJA DE ENTRADA
                # ==============================
                elif op == "7":
                    print("\n--- BANDEJA DE ENTRADA ---")
                    usuario.carpetas.mostrar_mensajes_bandeja()

                # ==============================
                # CERRAR SESIÓN
                # ==============================
                elif op == "8":
                    print("✔ Sesión cerrada.")
                    break

                else:
                    print("❌ Opción inválida.")

        # ==============================
        # CREAR USUARIO
        # ==============================
        elif opcion == "2":
            nombre = input("Nuevo nombre de usuario: ").strip()

            if nombre in usuarios:
                print("❌ Ese usuario ya existe.")
                continue

            usuarios[nombre] = Usuario(nombre)
            print("✔ Usuario creado correctamente.")

        # ==============================
        # SALIR
        # ==============================
        elif opcion == "3":
            print("\nSaliendo del sistema… Gracias por usar el Cliente de Correo UNaB.")
            break

        else:
            print("❌ Opción inválida.")


# ==============================
#   EJECUCIÓN
# ==============================

if __name__ == "__main__":
    main()

