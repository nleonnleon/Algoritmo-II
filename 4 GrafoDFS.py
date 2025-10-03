import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo dirigido
g = nx.DiGraph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(5, 7)
g.add_edge(4, 8)
g.add_edge(3, 8)



# Implementación de DFS
def dfs(grafo, nodo_inicial, visitado=None):    
    if visitado is None:
        visitado = set()
    visitado.add(nodo_inicial)
    print(nodo_inicial, end=' ')
    for vecino in grafo.neighbors(nodo_inicial):
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)
    return visitado

    # Ejemplo de uso
print("Recorrido DFS a partir del nodo 1:")         
dfs(g, 1)           
print() # Nueva línea al final del recorrido    


# Dibujar el grafo
nx.draw_shell(g, with_labels=True)
plt.show() # Muestra el gráfico
