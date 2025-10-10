import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo dirigido
g = nx.DiGraph()

g.add_node("Lima")
g.add_node("Trujillo")
g.add_node("Cajamarca")
g.add_node("Amazonas")
g.add_node("Chiclayo")


g.add_edge("Lima","Trujillo" , relation =560)
g.add_edge("Trujillo","Cajamarca" , relation =300)
g.add_edge("Cajamarca","Amazonas" , relation =230)   
g.add_edge("Amazonas","Chiclayo" , relation =797)           
g.add_edge("Chiclayo","Lima" , relation =777)         


# Función de consumo de combustible
def consumo_combustible(kilometros):
    return 0.102 * kilometros  # galones

# Función para calcular el costo total del viaje
def calcular_costo_camino(grafo, camino, precio_por_galon):
    distancia_total = 0
    for i in range(len(camino) - 1): # recorre la lista de ciudades desde el primer hasta el penúltimo índice
        origen = camino[i]
        destino = camino[i + 1] #- Se define el par de ciudades entre las que se va a calcular la distancia

        distancia = grafo[origen][destino]['relation'] #- Se accede al grafo para obtener la distancia entre origen y destino

        distancia_total += distancia
    galones = consumo_combustible(distancia_total)
    costo_total = galones * precio_por_galon
    print(f"Camino: {' → '.join(camino)}")
    print(f"Distancia total: {distancia_total} km")
    print(f"Galones consumidos: {galones:.2f}")
    print(f"Costo total del viaje: S/ {costo_total:.2f}")



precio_galon = 18.50  # Precio en soles por galón

ruta = ["Lima", "Trujillo", "Cajamarca", "Amazonas", "Chiclayo", "Lima"]
calcular_costo_camino(g, ruta, precio_galon)

   


# Posiciones para los nodos
pos = nx.spring_layout(g)

# Dibujar nodos y arcos
nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, arrows=True)

# Extraer las etiquetas de los arcos
edge_labels = nx.get_edge_attributes(g, 'relation')

# Dibujar las etiquetas en los arcos
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='red')


plt.show() # Muestra el gráfico