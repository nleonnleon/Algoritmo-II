
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Crear los nodos
raiz = Nodo(2)  # Altura 0
raiz.izquierda = Nodo(5)  # Altura 1
raiz.derecha = Nodo(7)    # Altura 1


# Función para calcular la profundidad del árbol
def profundidad(nodo):
    if nodo is None:
        return -1  # Si no hay nodo, la profundidad es -1
    else:
        izquierda = profundidad(nodo.izquierda)
        derecha = profundidad(nodo.derecha)
        return 1 + max(izquierda, derecha)

# Función para imprimir la profundidad
def imprimir_profundidad(nodo):
    print("La profundidad del árbol es:", profundidad(nodo))


# Ejecutar las funciones
imprimir_profundidad(raiz)



