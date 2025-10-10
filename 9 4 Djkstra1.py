import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo dirigido
g = nx.DiGraph()

g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E") 
g.add_node("F")


g.add_edge("A","B" , relation =400)
g.add_edge("A","E" , relation =200)
g.add_edge("B","E" , relation =100)   
g.add_edge("B","C" , relation =500)           
g.add_edge("B","E" , relation =100) 
g.add_edge("E","C" , relation =800)
g.add_edge("E","D" , relation =1000) 
g.add_edge("D","C" , relation =200)
g.add_edge("C","F" , relation =600)     
g.add_edge("D","F" , relation =300)            


# Aplicar Dijkstra para encontrar el camino más corto de A a F
shortest_path = nx.dijkstra_path(g, source="A", target="F", weight="relation")
shortest_distance = nx.dijkstra_path_length(g, source="A", target="F", weight="relation")

# Mostrar resultados
print("Camino más corto de A a F:", " → ".join(shortest_path))
print("Valor total del camino:", shortest_distance)



# Visualización del grafo
#pos = nx.spring_layout(g)
plt.title("Grafo con mínimos cruces de aristas")

# Usar un layout que minimiza cruces de aristas
pos = nx.kamada_kawai_layout(g)


# Dibujar nodos y aristas
nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, arrows=True)

# Etiquetas de las aristas
edge_labels = nx.get_edge_attributes(g, 'relation')
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='red')

# Mostrar el grafo

plt.show()



   