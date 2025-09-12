class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Crear los nodos
raiz = Nodo(2)  # Altura 0
raiz.izquierda = Nodo(5)  # Altura 1
raiz.derecha = Nodo(7)    # Altura 1    


raiz.izquierda.izquierda = Nodo(3)  # Altura 2      
raiz.izquierda.derecha = Nodo(4)    # Altura 2
raiz.derecha.izquierda = Nodo(6)    # Altura 2
raiz.derecha.derecha = Nodo(9)      # Altura 2

raiz.derecha.derecha.derecha = Nodo(10) # Altura 3


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


# 🔍 Función para recorrido preorden
def recorrido_preorden(nodo):
    if nodo:
        print(nodo.valor, end=' ')
        recorrido_preorden(nodo.izquierda)
        recorrido_preorden(nodo.derecha)

# Ejecutar funciones
print("Recorrido en preorden:")
recorrido_preorden(raiz)    
print()  # Nueva línea para mejor formato   
imprimir_profundidad(raiz)
