import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo dirigido
g = nx.DiGraph()

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(5, 7)
g.add_edge(4, 8)
g.add_edge(3, 8)


# Encontrar amigos directos (nodos adyacentes) del nodo 4
amigos_salientes = list(g.successors(4))
print("Amigos directos salientes del nodo 4:", amigos_salientes)
print("Cantidad:", len(amigos_salientes))

#   Encontrar amigos directos entrantes (nodos que apuntan al nodo 4)
amigos_entrantes = list(g.predecessors(4))
print("Amigos directos entrantes del nodo 4:", amigos_entrantes)
print("Cantidad:", len(amigos_entrantes))

#   Encontrar todos los amigos directos (tanto entrantes como salientes)
amigos_totales = set(amigos_salientes + amigos_entrantes)
print("Total de amigos directos del nodo 4:", amigos_totales)
print("Cantidad:", len(amigos_totales))



# Dibujar el grafo
nx.draw(g, with_labels=True)
plt.show() # Muestra el gráfico

