import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo dirigido
g = nx.DiGraph()

g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E") 



g.add_edge("A","C" , relation =8)
g.add_edge("A","B" , relation =4)
g.add_edge("B","C" , relation =1)   
g.add_edge("B","D" , relation =2)           
g.add_edge("D","C" , relation =4) 
g.add_edge("D","E" , relation =7)
g.add_edge("C","E" , relation =2) 
 

 # Representamos el infinito con un valor numérico grande
INF = float('inf')

def floyd_warshall(graph):
    """
    Implementa el algoritmo de Floyd-Warshall para encontrar las distancias
    más cortas entre todos los pares de vértices en un grafo.

    Args:
        graph: Una matriz de adyacencia donde graph[i][j] es el peso de la arista
               de i a j. Si no hay arista, el valor es INF.

    Returns:
        Una matriz que contiene las distancias más cortas entre todos los pares de vértices.
    """
    num_vertices = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph)) # Copiar la matriz de adyacencia

    # Itera a través de todos los nodos como posibles nodos intermedios
    for k in range(num_vertices):
        # Itera a través de todos los pares de nodos
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Si el nodo k está en el camino más corto de i a j, actualiza la distancia
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Los valores son los pesos de las aristas
graph = [
    [0, 4, 8, INF,INF],
    [4, 0, 1, 2,INF],
    [8, 1, 0, 4,2],
    [INF, 2, 4, 0,7],
    [INF,INF,2,7,0]
]

# Calcular las distancias más cortas
shortest_distances = floyd_warshall(graph)

# Imprimir el resultado
print("Distancias más cortas entre todos los pares de nodos:")
for row in shortest_distances:
    print(row)

# Usar un layout que minimiza cruces de aristas
pos = nx.kamada_kawai_layout(g)

plt.title("Grafo con mínimas cruces de aristas")

# Dibujar nodos y aristas
nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, arrows=True)

# Etiquetas de las aristas
edge_labels = nx.get_edge_attributes(g, 'relation')
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='red')

# Mostrar el grafo

plt.show()