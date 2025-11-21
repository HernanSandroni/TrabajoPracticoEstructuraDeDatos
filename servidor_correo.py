from mensaje import Mensaje

class ServidorCorreo:
    def __init__(self):
        # Usuarios registrados en el servidor
        self.usuarios = {}

        # Grafo de la red de servidores
        # Diccionario de listas de adyacencia
        self.red = {}

    # =====================================================
    #   REGISTRAR USUARIO
    # =====================================================
    def registrar_usuario(self, usuario):
        self.usuarios[usuario.nombre] = usuario

    # =====================================================
    #   AGREGAR CONEXIÓN ENTRE SERVIDORES (GRAFO)
    # =====================================================
    def agregar_conexion(self, servidor1, servidor2):
        # Grafo no dirigido
        if servidor1 not in self.red:
            self.red[servidor1] = []
        if servidor2 not in self.red:
            self.red[servidor2] = []

        self.red[servidor1].append(servidor2)
        self.red[servidor2].append(servidor1)

    # =====================================================
    #   ENVIAR MENSAJE ENTRE USUARIOS LOCALES
    # =====================================================
    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo, urgente=False):
        if remitente not in self.usuarios:
            print("El remitente no existe.")
            return

        if destinatario not in self.usuarios:
            print("El destinatario no existe.")
            return

        mensaje = Mensaje(remitente, destinatario, asunto, cuerpo, urgente)

        # El destinatario recibe el mensaje
        self.usuarios[destinatario].recibir_mensaje(mensaje)

        print(f"Mensaje enviado de {remitente} a {destinatario}.")

    # =====================================================
    #   BFS PARA RECORRER LA RED
    # =====================================================
    def bfs(self, inicio):
        if inicio not in self.red:
            print("Ese servidor no existe en la red.")
            return []

        visitados = set()
        cola = [inicio]
        resultado = []

        while cola:
            actual = cola.pop(0)
            if actual not in visitados:
                visitados.add(actual)
                resultado.append(actual)

                # agrego los vecinos
                for vecino in self.red[actual]:
                    if vecino not in visitados:
                        cola.append(vecino)

        return resultado

    # =====================================================
    #   DFS PARA RECORRER LA RED
    # =====================================================
    def dfs(self, inicio, visitados=None, resultado=None):
        if inicio not in self.red:
            print("Ese servidor no existe en la red.")
            return []

        if visitados is None:
            visitados = set()
        if resultado is None:
            resultado = []

        visitados.add(inicio)
        resultado.append(inicio)

        for vecino in self.red[inicio]:
            if vecino not in visitados:
                self.dfs(vecino, visitados, resultado)

        return resultado

    # =====================================================
    #   SIMULAR ENVÍO EN LA RED CON BFS/DFS
    # =====================================================
    def simular_envio_red(self, nombre_usuario):
        print("\n=== Simulación de Envío por la Red ===")

        if not self.red:
            print("La red de servidores está vacía.")
            return

        print("\nServidores disponibles:", list(self.red.keys()))

        servidor_origen = input("Ingrese un servidor de origen: ")
        algoritmo = input("Usar BFS o DFS?: ").upper()

        if algoritmo == "BFS":
            recorrido = self.bfs(servidor_origen)
        elif algoritmo == "DFS":
            recorrido = self.dfs(servidor_origen)
        else:
            print("Algoritmo no válido.")
            return

        print(f"\nRecorrido ({algoritmo}):", " -> ".join(recorrido))
        print(f"Simulación completada para el usuario {nombre_usuario}.\n")
