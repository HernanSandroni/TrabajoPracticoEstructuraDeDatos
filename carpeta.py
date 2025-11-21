from mensaje import Mensaje

class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []      # lista de Mensaje
        self.subcarpetas = []   # lista de Carpeta (árbol general)

    # =====================================================
    #   MOSTRAR CARPETAS (RECORRIDO RECURSIVO)
    # =====================================================
    def mostrar(self, nivel=0):
        print("   " * nivel + f"- {self.nombre}")
        for msg in self.mensajes:
            print("   " * (nivel + 1) + f"* {msg.asunto} (de {msg.remitente})")

        for sub in self.subcarpetas:
            sub.mostrar(nivel + 1)

    # =====================================================
    #   AGREGAR SUBCARPETA
    # =====================================================
    def agregar_subcarpeta(self, nombre):
        nueva = Carpeta(nombre)
        self.subcarpetas.append(nueva)
        return nueva

    # =====================================================
    #   AGREGAR MENSAJE
    # =====================================================
    def agregar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    # =====================================================
    #   BUSCAR RECURSIVAMENTE MENSAJES
    # =====================================================
    def buscar_recursivo(self, criterio):
        encontrados = []

        # Buscar en mensajes de esta carpeta
        for msg in self.mensajes:
            if criterio.lower() in msg.asunto.lower() or criterio.lower() in msg.remitente.lower():
                encontrados.append(msg)

        # Buscar en subcarpetas recursivamente
        for sub in self.subcarpetas:
            encontrados.extend(sub.buscar_recursivo(criterio))

        return encontrados

    # =====================================================
    #   MOVER MENSAJE A OTRA CARPETA (REC.)
    # =====================================================
    def mover_mensaje(self, mensaje, destino_nombre):
        # Si el mensaje está en esta carpeta, moverlo
        if mensaje in self.mensajes:
            self.mensajes.remove(mensaje)
            destino = self.buscar_carpeta(destino_nombre)
            if destino:
                destino.agregar_mensaje(mensaje)
                return True
            else:
                print(f"No existe la carpeta destino: {destino_nombre}")
                return False

        # Si no está, buscar recursivamente
        for sub in self.subcarpetas:
            if sub.mover_mensaje(mensaje, destino_nombre):
                return True

        return False

    # =====================================================
    #   BUSCAR CARPETA POR NOMBRE (REC.)
    # =====================================================
    def buscar_carpeta(self, nombre):
        if self.nombre == nombre:
            return self

        for sub in self.subcarpetas:
            encontrada = sub.buscar_carpeta(nombre)
            if encontrada:
                return encontrada

        return None

    # =====================================================
    #   APLICAR FILTRO RECURSIVO
    #   campo: "remitente" o "asunto"
    # =====================================================
    def aplicar_filtro_recursivo(self, campo, palabra, carpeta_destino):

        destino = self.buscar_carpeta(carpeta_destino)
        if not destino:
            print(f"[ERROR] Carpeta destino '{carpeta_destino}' no encontrada.")
            return

        # Primero reviso MIS mensajes
        mover = []
        for msg in self.mensajes:
            valor = getattr(msg, campo)
            if palabra.lower() in valor.lower():
                mover.append(msg)

        # Muevo los que coincidieron
        for msg in mover:
            self.mensajes.remove(msg)
            destino.agregar_mensaje(msg)

        # Luego aplico recursivamente en subcarpetas
        for sub in self.subcarpetas:
            sub.aplicar_filtro_recursivo(campo, palabra, carpeta_destino)
