import heapq

class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def push(self, mensaje, prioridad):
        # heapq usa una tupla (prioridad, elemento)
        heapq.heappush(self.cola, (prioridad, mensaje))

    def pop(self):
        if self.cola:
            return heapq.heappop(self.cola)[1]
        return None

    def esta_vacia(self):
        return len(self.cola) == 0
