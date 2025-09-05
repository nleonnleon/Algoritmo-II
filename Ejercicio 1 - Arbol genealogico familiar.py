# arbol binario para árbol genealógico familiar
# Cada nodo tiene como máximo dos hijos

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None

def buscar(nodo, nombre):
    if nodo is None:
        return False
    if nodo.nombre == nombre:
        return True
    return buscar(nodo.izquierda, nombre) or buscar(nodo.derecha, nombre)

def profundidad(nodo):
    if nodo is None:
        return 0
    return 1 + max(profundidad(nodo.izquierda), profundidad(nodo.derecha))

# Datos de prueba
raiz = Nodo("Abuelo")
raiz.izquierda = Nodo("Padre")
raiz.derecha = Nodo("Tío")
raiz.izquierda.izquierda = Nodo("Martín")
raiz.izquierda.derecha = Nodo("Hermana de Martín")

print(buscar(raiz, "Martín"))  # True
print(profundidad(raiz))       # 3



def imprimirArbolBinario(nodo, nivel=0):
    if nodo is not None:
        print("  " * nivel + nodo.nombre)
        imprimirArbolBinario(nodo.izquierda, nivel + 1)
        imprimirArbolBinario(nodo.derecha, nivel + 1)




# Imprimir el árbol
imprimirArbolBinario(raiz)