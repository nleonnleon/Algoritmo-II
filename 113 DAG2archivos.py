import networkx as nx

def construir_grafo_desde_archivo(nombre_archivo):
    G = nx.DiGraph()
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split()
            if len(partes) == 2:
                origen, destino = partes
                G.add_edge(origen, destino)
    return G

def leer_datos_tareas(nombre_archivo):
    datos = {}
    with open(nombre_archivo, 'r') as archivo:
        next(archivo)  # Saltar encabezado
        for linea in archivo:
            partes = linea.strip().split()
            if len(partes) == 4:
                tarea, costo, tiempo, esfuerzo = partes
                datos[tarea] = {
                    'Costo': float(costo),
                    'Tiempo': float(tiempo),
                    'Esfuerzo': float(esfuerzo)
                }
    return datos

# Construir grafo y leer datos
G = construir_grafo_desde_archivo('C:/Users/Leo/Desktop/Grafo/tareas.txt')
datos = leer_datos_tareas('C:/Users/Leo/Desktop/Grafo/trabajo.txt')

# Verificar si es DAG y mostrar orden con atributos
if nx.is_directed_acyclic_graph(G):
    orden = list(nx.topological_sort(G))
    print("🧩 Orden de tareas con atributos:")
    for i, tarea in enumerate(orden, 1):
        info = datos.get(tarea, {'Costo': '-', 'Tiempo': '-', 'Esfuerzo': '-'})
        print(f"{i}. {tarea} → Costo: {info['Costo']}, Tiempo: {info['Tiempo']}, Esfuerzo: {info['Esfuerzo']}")
else:
    print("❌ El grafo tiene ciclos y no se puede ordenar topológicamente.")
