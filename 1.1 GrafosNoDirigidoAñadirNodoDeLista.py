import networkx as nx #Para estructuras dinámicas y redes
import matplotlib.pyplot as plt  # Para visualización
# Crear un grafo no dirigido
G = nx.Graph()

# Añadir nodos individuales
G.add_node("A")
G.add_node("B")


# Añadir múltiples nodos desde una lista
G.add_nodes_from(["C", "D", "E"])

# Dibujar el grafo
nx.draw_shell(G, with_labels=True)

plt.show() # Muestra el gráfico