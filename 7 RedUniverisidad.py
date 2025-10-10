import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo dirigido
g = nx.DiGraph()

g.add_node("Profesor A")
g.add_node("Profesor B")
g.add_node("Profesor C")
g.add_node("Profesor D")

g.add_edge("Profesor A","Profesor B" , relation ="amigo")
g.add_edge("Profesor B","Profesor C" , relation ="trabajo")
g.add_edge("Profesor C","Profesor D" , relation ="amigo")   
g.add_edge("Profesor A","Profesor D" , relation ="trabajo")

# Posiciones para los nodos
pos = nx.spring_layout(g)

# Dibujar nodos y arcos
nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, arrows=True)

# Extraer las etiquetas de los arcos
edge_labels = nx.get_edge_attributes(g, 'relation')

# Dibujar las etiquetas en los arcos
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='red')


plt.show() # Muestra el gráfico
