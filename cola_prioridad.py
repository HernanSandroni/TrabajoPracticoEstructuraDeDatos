import heapq

class ColaPrioridad:
    def __init__(self):
        """Inicializa una cola de prioridad vacía"""
        self._cola = []

    def agregar_mensaje(self, mensaje, prioridad):
        """
        Agrega un mensaje a la cola con su prioridad.
        prioridad: menor número = mayor prioridad (ej. 1 = urgente)
        """
        heapq.heappush(self._cola, (prioridad, mensaje))

    def extraer_mensaje(self):
        """
        Extrae el mensaje con mayor prioridad (menor número).
        Retorna None si la cola está vacía.
        """
        if self._cola:
            return heapq.heappop(self._cola)[1]
        return None

    def esta_vacia(self):
        """Devuelve True si la cola está vacía"""
        return len(self._cola) == 0
