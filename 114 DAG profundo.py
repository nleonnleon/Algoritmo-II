import networkx as nx
import matplotlib.pyplot as plt

# Crear un dígrafo
g = nx.DiGraph()

# Agregar nodos (tareas)
tareas = ["A","B","C","D","E","F","G","H","I","J","K"]
#   Agregar nodos al grafo
g.add_nodes_from(tareas)

# Agregar aristas (dependencias)
g.add_edge("A", "B")
g.add_edge("A", "D")
g.add_edge("A", "C") 

g.add_edge("B", "E")
#g.add_edge("B", "D")
g.add_edge("B", "F")
g.add_edge("F", "I")
g.add_edge("F", "J")
            
g.add_edge("C", "J") 
g.add_edge("D", "G")
g.add_edge("D", "H")  

g.add_edge("G", "K")
g.add_edge("J", "K")




# Ordenación topológica
orden = list(nx.topological_sort(g))

# Imprimir el orden de las tareas
print("Orden de tareas:")
# 5. Ordenar Topológicamente
#


    
# Determinar posiciones para la visualización
pos = nx.kamada_kawai_layout(g)

# Visualización del grafo
plt.figure(figsize=(10, 6))
plt.title("Dependencias del Proyecto: Videojuego")

# Dibujar el grafo con etiquetas
nx.draw(g, pos, with_labels=True, node_color='lightcoral', node_size=1000, font_size=10,  arrowsize=20, width=2)


#mostrar el grafo
plt.show()
