import networkx as nx
import matplotlib.pyplot as plt

# Crear un dígrafo
G = nx.DiGraph()

# Agregar nodos (tareas)
tareas = [
    "Escribir guion",
    "Hacer storyboard",
    "Crear fondos",
    "Crear Sonidos",
    "Crear lógica de APUS",
    "Crear lógica de Illas",
    "Integrar",
       "Publicar"
]
#   Agregar nodos al grafo
G.add_nodes_from(tareas)

# Agregar aristas (dependencias)
G.add_edge("Escribir guion", "Hacer storyboard")
G.add_edge("Hacer storyboard", "Crear fondos")
G.add_edge("Crear fondos", "Crear Sonidos")
G.add_edge("Crear Sonidos", "Crear lógica de APUS")
G.add_edge("Crear lógica de APUS", "Crear lógica de Illas")
G.add_edge("Crear lógica de Illas", "Integrar")             
G.add_edge("Integrar", "Publicar")     

# Ordenación topológica
orden = list(nx.topological_sort(G))

# Imprimir el orden de las tareas
print("Orden de tareas:")
for i, tarea in enumerate(orden, 1):
    print(f"{i}. {tarea}")
    
# Determinar posiciones para la visualización
pos = nx.spring_layout(G)


# Visualización del grafo
plt.figure(figsize=(10, 6))
plt.title("Dependencias del Proyecto: Videojuego")

# Dibujar el grafo con etiquetas
nx.draw(G, pos, with_labels=True, node_color='lightcoral', node_size=2000, font_size=10, font_weight='bold', arrowsize=20)


#mostrar el grafo
plt.show()
