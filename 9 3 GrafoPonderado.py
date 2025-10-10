import networkx as nx

# Crear un grafo no dirigido
G = nx.Graph()

# Añadir nodos
G.add_node('A')
G.add_node('B')
G.add_node('C')

# Añadir aristas con pesos
G.add_edge('A', 'B', weight=5)
G.add_edge('B', 'C', weight=10)
G.add_edge('A', 'C', weight=7)

# Para un grafo dirigido (ejemplo con ciudades)
D = nx.DiGraph()
D.add_edge('Madrid', 'Barcelona', distance=600)
D.add_edge('Barcelona', 'Madrid', distance=600) # El peso puede ser el mismo en ambas direcciones

print("Grafo no dirigido:")
print(G.edges(data=True)) # Muestra las aristas con sus pesos
print("\nGrafo dirigido:")
print(D.edges(data=True))