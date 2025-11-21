from carpeta import Carpeta
from mensaje import Mensaje
from cola_prioridad import ColaPrioridad

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carpetas = Carpeta("Bandeja de entrada")   # raíz del árbol de carpetas
        self.filtros = []                                # lista de filtros automáticos
        self.urgentes = ColaPrioridad()                  # cola de prioridad
        self.enviados = []                               # historial opcional

    # =====================================================
    #   MOSTRAR CARPETAS (RECORRIDO RECURSIVO)
    # =====================================================
    def mostrar_carpetas(self):
        print("\n=== CARPETAS DE", self.nombre, "===")
        self.carpetas.mostrar()

    # =====================================================
    #   BUSCAR MENSAJES (RECURSIVO)
    # =====================================================
    def buscar_mensajes(self, criterio):
        print(f"\n=== Buscando '{criterio}' en todas las carpetas ===")
        resultados = self.carpetas.buscar_recursivo(criterio)

        if resultados:
            for msg in resultados:
                print(msg)
        else:
            print("No se encontraron mensajes.")

    # =====================================================
    #   APLICAR FILTROS AUTOMÁTICOS
    # =====================================================
    def aplicar_filtros(self):
        if not self.filtros:
            print("No hay filtros configurados.")
            return
        
        print("\nAplicando filtros automáticos...")

        for filtro in self.filtros:
            campo, palabra, carpeta_destino = filtro
            self.carpetas.aplicar_filtro_recursivo(campo, palabra, carpeta_destino)

        print("Filtros aplicados con éxito.")

    # =====================================================
    #   MENSAJES URGENTES (COLA DE PRIORIDAD)
    # =====================================================
    def agregar_urgente(self, mensaje):
        self.urgentes.push(mensaje, prioridad=1)

    def ver_urgentes(self):
        print("\n=== MENSAJES URGENTES ===")
        if self.urgentes.esta_vacia():
            print("No hay mensajes urgentes.")
        else:
            while not self.urgentes.esta_vacia():
                print(self.urgentes.pop())

    # =====================================================
    #   AGREGAR MENSAJE A BANDEJA DE ENTRADA
    # =====================================================
    def recibir_mensaje(self, mensaje):
        # Si el mensaje es urgente, va a la cola
        if mensaje.urgente:
            self.agregar_urgente(mensaje)

        # Siempre entra a "Bandeja de entrada"
        self.carpetas.agregar_mensaje(mensaje)

        # Se aplican filtros automáticamente
        self.aplicar_filtros()

    # =====================================================
    #   UTILIDAD
    # =====================================================
    def __str__(self):
        return f"Usuario({self.nombre})"
