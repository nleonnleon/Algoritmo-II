import networkx as nx
import matplotlib.pyplot as plt # Para visualización
#g = nx.Graph()
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

# Crear figura y establecer título
plt.title("Grafo Dirigido y No Ponderado")  # Esto pone el título en el gráfico

# Dibujar el grafo
nx.draw_shell(g, with_labels=True)

plt.show() # Muestra el gráfico