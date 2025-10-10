import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo dirigido
g = nx.Graph()

# Agregar nodos
g.add_nodes_from(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

# Agregar aristas con pesos (usando 'weight' en lugar de 'relation')

g.add_edge("1", "2", weight=3)
g.add_edge("1", "4", weight=5)
g.add_edge("1", "3", weight=5)
g.add_edge("2", "3", weight=9)
g.add_edge("2", "7", weight=3)
g.add_edge("3", "4", weight=5)
g.add_edge("3", "8", weight=3)
g.add_edge("3", "6", weight=5)
g.add_edge("7", "5", weight=3)
g.add_edge("7", "8", weight=5)
g.add_edge("5", "9", weight=5)
g.add_edge("6", "9", weight=8)
g.add_edge("8", "9", weight=6)
g.add_edge("4", "6", weight=15)


# Calcular rutas más cortas desde el nodo "1"
shortest_paths = nx.single_source_dijkstra_path(g, source="1", weight="weight")
shortest_distances = nx.single_source_dijkstra_path_length(g, source="1", weight="weight")

# Mostrar resultados
print("Rutas más cortas desde el nodo '1':")
for target, path in shortest_paths.items():
    print(f"→ Nodo {target}: Ruta {path}, Costo total = {shortest_distances[target]}")





# Crear figura y establecer título
plt.title("Grafo No Dirigido y Ponderado")  # Esto pone el título en el gráfico

# Usar un layout que minimiza cruces de aristas
pos = nx.kamada_kawai_layout(g)

# Dibujar el grafo
nx.draw(g, pos,with_labels=True)

edge_labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

plt.show() # Muestra el gráfico

