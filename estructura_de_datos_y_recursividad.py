class Mensaje:
    """Representa un mensaje de correo electrónico."""
    def __init__(self, remitente, destinatario, asunto, contenido):
        self._remitente = remitente
        self._destinatario = destinatario
        self._asunto = asunto
        self._contenido = contenido

    @property
    def remitente(self):
        return self._remitente

    @property
    def destinatario(self):
        return self._destinatario

    @property
    def asunto(self):
        return self._asunto

    @property
    def contenido(self):
        return self._contenido


class Carpeta:
    """Representa una carpeta de correo que puede contener mensajes y subcarpetas."""

    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []
        self._subcarpetas = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def mensajes(self):
        return self._mensajes

    @property
    def subcarpetas(self):
        return self._subcarpetas

    def agregar_subcarpeta(self, subcarpeta):
        """Agrega una subcarpeta al nodo actual."""
        self._subcarpetas.append(subcarpeta)

    def agregar_mensaje(self, mensaje):
        """Agrega un mensaje a esta carpeta."""
        self._mensajes.append(mensaje)

    def mover_mensaje(self, asunto, carpeta_destino):
        """
        Mueve un mensaje de esta carpeta a otra carpeta.
        Retorna True si el mensaje se movió, False si no se encontró.
        """
        for msg in self._mensajes:
            if msg.asunto == asunto:
                carpeta_destino.agregar_mensaje(msg)
                self._mensajes.remove(msg)
                return True
        return False

    def buscar_recursivo(self, criterio, valor):
        """
        Busca mensajes recursivamente por un criterio (remitente o asunto) en esta carpeta y subcarpetas.
        Retorna una lista de mensajes encontrados.
        """
        encontrados = []
        for msg in self._mensajes:
            if getattr(msg, criterio) == valor:
                encontrados.append(msg)
        for sub in self._subcarpetas:
            encontrados.extend(sub.buscar_recursivo(criterio, valor))
        return encontrados

    def listar_estructura(self, nivel=0):
        """Imprime la estructura de carpetas y cantidad de mensajes en cada una."""
        print("  " * nivel + f"- {self._nombre} ({len(self._mensajes)} mensajes)")
        for sub in self._subcarpetas:
            sub.listar_estructura(nivel + 1)


class Usuario:
    """Representa un usuario con un nombre, email y carpeta principal Inbox."""

    def __init__(self, nombre, email):
        self._nombre = nombre
        self._email = email
        self._root = Carpeta("Inbox")  # Carpeta principal

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @property
    def root(self):
        return self._root

    def enviar_mensaje(self, destinatario, asunto, contenido):
        """Crea un mensaje y lo agrega a la carpeta Inbox del usuario remitente."""
        mensaje = Mensaje(self._nombre, destinatario.nombre, asunto, contenido)
        self._root.agregar_mensaje(mensaje)
        print(f"{self._nombre} envió mensaje a {destinatario.nombre} con asunto '{asunto}'")


# --- Menú de prueba ---
if __name__ == "__main__":
    usuario1 = Usuario("Ana", "ana@mail.com")
    usuario2 = Usuario("Luis", "luis@mail.com")

    # Crear subcarpetas
    proyectos = Carpeta("Proyectos")
    personal = Carpeta("Personal")
    usuario1.root.agregar_subcarpeta(proyectos)
    usuario1.root.agregar_subcarpeta(personal)

    while True:
        print("\n--- MENÚ ---")
        print("1. Enviar mensaje")
        print("2. Listar carpetas")
        print("3. Buscar mensajes por remitente")
        print("4. Buscar mensajes por asunto")
        print("5. Mover mensaje")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            asunto = input("Asunto: ")
            contenido = input("Contenido: ")
            usuario1.enviar_mensaje(usuario2, asunto, contenido)
        elif opcion == "2":
            usuario1.root.listar_estructura()
        elif opcion == "3":
            remitente = input("Ingrese el nombre del remitente a buscar: ")
            encontrados = usuario1.root.buscar_recursivo("remitente", remitente)
            print(f"Mensajes encontrados: {len(encontrados)}")
            for m in encontrados:
                print(f"- {m.asunto} de {m.remitente}")
        elif opcion == "4":
            asunto = input("Ingrese el asunto a buscar: ")
            encontrados = usuario1.root.buscar_recursivo("asunto", asunto)
            print(f"Mensajes encontrados: {len(encontrados)}")
            for m in encontrados:
                print(f"- {m.asunto} de {m.remitente}")
        elif opcion == "5":
            asunto = input("Asunto del mensaje a mover: ")
            carpeta_destino_nombre = input("Nombre de la carpeta destino: ")
            destino = usuario1.root.buscar_recursivo("nombre", carpeta_destino_nombre)
            if destino:
                moved = usuario1.root.mover_mensaje(asunto, destino[0])  # Usamos el primer resultado
                if moved:
                    print(f"Mensaje '{asunto}' movido a '{carpeta_destino_nombre}'")
                else:
                    print("Mensaje no encontrado")
            else:
                print("Carpeta destino no encontrada")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")
