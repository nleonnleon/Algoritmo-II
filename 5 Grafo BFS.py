import networkx as nx # type: ignore
import matplotlib.pyplot as plt
from collections import deque  # Para la cola en BFS

# Crear un grafo no dirigido
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

# Función BFS
def bfs(grafo, nodo_inicial):
    visitado = set()
    cola = deque([nodo_inicial])
    
    while cola:
        nodo = cola.popleft()
        if nodo not in visitado:
            print(nodo, end=' ')
            visitado.add(nodo)
            for vecino in grafo.neighbors(nodo):
                if vecino not in visitado:
                    cola.append(vecino)

# Mostrar recorrido BFS desde el nodo 1
print("Recorrido BFS desde el nodo 1:")
bfs(g, 1)

# Dibujar el grafo
nx.draw_shell(g, with_labels=True)
plt.show()

