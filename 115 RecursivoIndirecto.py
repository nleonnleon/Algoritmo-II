import networkx as nx

# Crear el grafo
g = nx.Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(5, 7)
g.add_edge(4, 8)
g.add_edge(3, 8)

# Estructuras globales para mantener estado
visitado = set()
cola = []

def procesar_nodo():
    if not cola:
        return
    nodo = cola.pop(0)
    if nodo not in visitado:
        print(f"Tarea: {nodo}")
        visitado.add(nodo)
        explorar_vecinos(nodo)
    procesar_nodo()  # Llamada recursiva indirecta

def explorar_vecinos(nodo):
    for vecino in g.neighbors(nodo):
        if vecino not in visitado:
            cola.append(vecino)
    # Llamada indirecta de vuelta
    # No procesamos aquí, solo agregamos a la cola

# Inicio del recorrido
cola.append(1)
procesar_nodo()
