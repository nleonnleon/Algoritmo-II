class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento

def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre);
    subarbol.hijos.append(Arbol(elemento))


def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if (arbolBuscado != None):
            return arbolBuscado
    return None
abuela = "Inocenta Arce"
hija1 = "Delia Lescano"
hija2 = "Sontos Lescano"
hija3 = "Vicenta Lescano"
nieto1 = "Ramiro Leon"
nieta2 = "Norma Leon"
nieta3 = "Rocio Leon"
nieto4 = "Rosario Sanchez"
nieto5 = "Julio Givar"    
nieto6 = "LuManuel Givar"    
arbol = Arbol(abuela)
agregarElemento(arbol, hija2, abuela)
agregarElemento(arbol, hija3, abuela)
agregarElemento(arbol, nieto4, hija2)
agregarElemento(arbol, hija1, abuela)
agregarElemento(arbol, nieto1, hija1)
agregarElemento(arbol, nieta2, hija1)
agregarElemento(arbol, nieta3, hija1)
agregarElemento(arbol, nieto5, hija3)
agregarElemento(arbol, nieto6, hija3)

def imprimirArbol(arbol, nivel=0):
    print("  " * nivel + arbol.elemento)
    for hijo in arbol.hijos:
        imprimirArbol(hijo, nivel + 1)

# Imprimir el árbol
imprimirArbol(arbol)
