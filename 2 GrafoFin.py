import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo no dirigido
G = nx.Graph()


# Añadir nodos individuales
G.add_node("A")
G.add_node("B")

# Añadir múltiples nodos desde una lista
G.add_nodes_from(["C", "D", "E"])

# Añadir aristas individuales
G.add_edge("A", "B")
G.add_edge("B", "C")

# Añadir múltiples aristas desde una lista de tuplas
G.add_edges_from([("C", "D"), ("D", "E"), ("E", "A")])

# Dibujar el grafo
nx.draw_shell(G, with_labels=True)

plt.show() # Muestra el gráfico