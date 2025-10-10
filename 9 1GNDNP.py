import networkx as nx #Para estructuras dinámicas y redes
import matplotlib.pyplot as plt  # Para visualización
# Crear un grafo no dirigido
G = nx.Graph()

# Añadir nodos individuales



# Añadir múltiples nodos desde una lista
G.add_nodes_from(["Juan", "Michael","Pedro", "Eduardo", "Julio", "Lino","Lucas", "Luis", "Carlos"])

# Añadir aristas individuales
G.add_edge("Juan", "Michael")
G.add_edge("Juan", "Lino")
G.add_edge("Juan", "Carlos")
G.add_edge("Pedro", "Eduardo")
G.add_edge("Eduardo", "Julio")      
G.add_edge("Eduardo", "Lucas")
G.add_edge("Lino", "Eduardo")  
G.add_edge("Lino", "Luis")
G.add_edge("Michael", "Pedro")
G.add_edge("Carlos", "Luis")
G.add_edge("Luis", "Lino")
   

numero_vetices=G.number_of_nodes()
numero_aristas=G.number_of_edges()

print("El numero de vertices es:",numero_vetices)
print("El numero de aristas es:",numero_aristas)

  
# Dibujar el grafo
nx.draw_planar(G, with_labels=True)

plt.show() # Muestra el gráfico