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

# Dibujar el grafo
nx.draw(g, with_labels=True)
plt.show() # Muestra el gráfico

