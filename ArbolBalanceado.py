class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.height = 1  # Altura inicial del nodo

class AVLTree:
    def insertar(self, raiz, valor):
        if not raiz:
            return NodoAVL(valor)
        elif valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = self.insertar(raiz.derecha, valor)

        raiz.height = 1 + max(self.obtener_altura(raiz.izquierda),
                              self.obtener_altura(raiz.derecha))

        balance = self.obtener_balance(raiz)

        # Rotaciones
        if balance > 1 and valor < raiz.izquierda.valor:
            return self.rotar_derecha(raiz)
        if balance < -1 and valor > raiz.derecha.valor:
            return self.rotar_izquierda(raiz)
        if balance > 1 and valor > raiz.izquierda.valor:
            raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)
        if balance < -1 and valor < raiz.derecha.valor:
            raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)

        return raiz

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.height

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.height = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.height = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.height = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.height = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y
    # Método para insertar desde el teclado
    def insertar_desde_teclado(self):
        try:
            valor = int(input("Ingrese un valor para insertar en el árbol AVL: "))
            self.raiz = self.insertar(self.raiz, valor)
            print(f"Valor {valor} insertado correctamente.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Función para imprimir el árbol en orden
def imprimir_en_orden(nodo):
    if nodo:
        imprimir_en_orden(nodo.izquierda)
        print(nodo.valor, end=' ')
        imprimir_en_orden(nodo.derecha)

# Insertar nodos
arbol = AVLTree()
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
    root = arbol.insertar(root, letter)



# Ejemplo de uso
if __name__ == "__main__":
    arbol = AVLTree()
    while True:
        arbol.insertar_desde_teclado()

# Imprimir el árbol en orden
imprimir_en_orden(root)
print()
