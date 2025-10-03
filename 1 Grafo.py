import networkx as nx
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo no dirigido
G = nx.Graph()


# Añadir nodos individuales
G.add_node("A")
G.add_node("B")

# dibujar el grafo
nx.draw(G, with_labels=True)
plt.show() # Muestra el gráfico