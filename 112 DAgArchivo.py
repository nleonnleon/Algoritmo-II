
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

def construir_grafo_desde_archivo(nombre_archivo):
  
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            origen, destino = linea.strip().split()
            G.add_edge(origen, destino)
    return G

# Construir el grafo desde el archivo
G = construir_grafo_desde_archivo('C:/Users/Leo/Desktop/Grafo/tareas.txt')


# Verificar si es un DAG antes de ordenar
if nx.is_directed_acyclic_graph(G):
    orden = list(nx.topological_sort(G))
    print("Orden de tareas:")
    for i, tarea in enumerate(orden, 1):
        print(f"{i}. {tarea}")
else:
    print("El grafo tiene ciclos y no se puede ordenar topológicamente.")



# Visualización del grafo
pos = nx.spring_layout(G)

#crear la figura
plt.figure(figsize=(10, 6))

plt.title("Dependencias del Proyecto: Videojuego")

nx.draw(G, pos, with_labels=True, node_color='lightcoral',
        node_size=2000, font_size=10, font_weight='bold', arrowsize=20)

plt.show()
