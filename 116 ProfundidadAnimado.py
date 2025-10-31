import networkx as nx # pyright: ignore[reportMissingModuleSource]
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear un grafo dirigido
g = nx.DiGraph()
g.add_edges_from([
    (1, 2), (2, 3), (2, 4), (1, 5), (5, 6),
    (5, 7), (6, 8), (6, 9)
])

# Preparar el recorrido DFS paso a paso
def dfs_steps(grafo, nodo_inicial):
    visitado = set()
    pasos = []

    def dfs(nodo):
        visitado.add(nodo)
        pasos.append(nodo)
        for vecino in grafo.neighbors(nodo):
            if vecino not in visitado:
                dfs(vecino)

    dfs(nodo_inicial)
    return pasos

# Obtener los pasos del recorrido
pasos_dfs = dfs_steps(g, 1)

# Configurar la visualización
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
pos = nx.shell_layout(g)

# Grafo completo a la izquierda
nx.draw(g, pos, with_labels=True, arrows=True, ax=ax1)
ax1.set_title("Grafo completo")

# Inicializar el recorrido DFS a la derecha
visited_nodes = []

def update(frame):
    ax2.clear()
    visited_nodes.append(pasos_dfs[frame])
    nx.draw(g, pos, with_labels=True, arrows=True, ax=ax2, node_color=[
        'lightcoral' if n in visited_nodes else 'lightgray' for n in g.nodes()
    ])
    ax2.set_title(f"DFS paso {frame + 1}: visitando {pasos_dfs[frame]}")

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(pasos_dfs), interval=1000, repeat=False)

plt.tight_layout()
plt.show()