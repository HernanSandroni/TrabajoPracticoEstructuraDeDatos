# grafo_servidores.py

class Servidor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []  # lista de servidores conectados

    def conectar(self, otro_servidor):
        """Conectar dos servidores (bidireccional)"""
        if otro_servidor not in self.conexiones:
            self.conexiones.append(otro_servidor)
        if self not in otro_servidor.conexiones:
            otro_servidor.conexiones.append(self)

# ----- BFS -----
def bfs(origen, destino):
    """
    Busca ruta de origen a destino usando BFS
    Retorna True si se puede llegar al destino
    """
    visitados = set()
    cola = [origen]

    while cola:
        actual = cola.pop(0)
        if actual == destino:
            return True
        visitados.add(actual)
        for vecino in actual.conexiones:
            if vecino not in visitados and vecino not in cola:
                cola.append(vecino)
    return False

# ----- DFS -----
def dfs(origen, destino):
    """
    Busca ruta de origen a destino usando DFS
    Retorna True si se puede llegar al destino
    """
    visitados = set()
    pila = [origen]

    while pila:
        actual = pila.pop()
        if actual == destino:
            return True
        visitados.add(actual)
        for vecino in actual.conexiones:
            if vecino not in visitados and vecino not in pila:
                pila.append(vecino)
    return False
