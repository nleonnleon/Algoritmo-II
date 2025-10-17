import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo no dirigido
g = nx.Graph()

# Calcular las distancias más cortas entre todos los pares de nodos
g.add_weighted_edges_from([
    (1, 7, 85), (7, 16, 61), (12, 16, 68), (10, 11, 34),
    (14, 10, 65), (6, 5, 99), (15, 13, 64), (1, 11, 60), 
    (16, 12, 85), (11, 12, 93), (1, 2, 79), (1, 15, 92),
    (17, 13, 89), (15, 6, 40), (15, 2, 99), (1, 3, 75),
    (15, 14, 69), (6, 17, 79), (2, 5, 59),  (1, 12, 82),
    (7, 10, 89), (5, 3, 73), (15, 12, 80)
    ])
 



# Usar un layout que minimiza cruces de aristas
pos = nx.kamada_kawai_layout(g)


# Crear subplots para comparar los grafos
fig, ax= plt.subplots(1,2)
fig.set_size_inches(12,6)


labels = nx.get_edge_attributes(g,'weight')

# Dibuja el grafo original
ax[0].set_title('Gráfica original')
nx.draw_kamada_kawai(g,with_labels=True, node_color='#bbbb22',node_size=500, ax=ax[0])
nx.draw_networkx_edge_labels(g,pos,ax=ax[0], edge_labels=labels)

# Dibuja el grafo originde mínimo peso
ax[1].set_title('Árbol de peso mínimo')


plt.show()