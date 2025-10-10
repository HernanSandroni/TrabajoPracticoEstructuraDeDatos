class Mensaje:
    def __init__(self, remitente, destinatario, asunto, contenido):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido


class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []
        self.subcarpetas = []

    def agregar_subcarpeta(self, subcarpeta):
        self.subcarpetas.append(subcarpeta)

    def agregar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    # Búsqueda recursiva por asunto o remitente
    def buscar_recursivo(self, criterio, valor):
        encontrados = []
        for msg in self.mensajes:
            if getattr(msg, criterio) == valor:
                encontrados.append(msg)
        for sub in self.subcarpetas:
            encontrados.extend(sub.buscar_recursivo(criterio, valor))
        return encontrados

    # Listar estructura de carpetas
    def listar_estructura(self, nivel=0):
        print("  " * nivel + f"- {self.nombre} ({len(self.mensajes)} mensajes)")
        for sub in self.subcarpetas:
            sub.listar_estructura(nivel + 1)


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.root = Carpeta("Inbox")  # Carpeta principal

    def enviar_mensaje(self, destinatario, asunto, contenido):
        mensaje = Mensaje(self.nombre, destinatario.nombre, asunto, contenido)
        self.root.agregar_mensaje(mensaje)
        print(f"{self.nombre} envió mensaje a {destinatario.nombre} con asunto '{asunto}'")

# --- Ejemplo de uso con menú ---
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
    print("4. Salir")
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
        print("Saliendo...")
        break
    else:
        print("Opción inválida")
