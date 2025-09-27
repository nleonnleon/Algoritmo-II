class MaxHeap:
    def __init__(self):
        self.heap = [0]  # Índice 0 no se usa
        self.tamano = 0

    def insertar(self, k):
        self.heap.append(k)
        self.tamano += 1
        self.subir(self.tamano)

    def subir(self, i):
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                # Intercambiar con el padre si es mayor
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def bajar(self, i):
        while (i * 2) <= self.tamano:
            hijo_mayor = self.hijoMayor(i)
            if self.heap[i] < self.heap[hijo_mayor]:
                self.heap[i], self.heap[hijo_mayor] = self.heap[hijo_mayor], self.heap[i]
            i = hijo_mayor

    def hijoMayor(self, i):
        if i * 2 + 1 > self.tamano:
            return i * 2
        else:
            if self.heap[i * 2] > self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMax(self):
        if self.tamano == 0:
            return None  # Heap vacío
        maximo = self.heap[1]
        self.heap[1] = self.heap[self.tamano]
        self.tamano -= 1
        self.heap.pop()
        self.bajar(1)
        return maximo

    def construirMonticulo(self, unaLista):
        self.tamano = len(unaLista)
        self.heap = [0] + unaLista[:]
        i = self.tamano // 2
        while i > 0:
            self.bajar(i)
            i -= 1

    def obtenerMax(self):
        if self.tamano == 0:
            return None
        return self.heap[1]

    def estaVacio(self):
        return self.tamano == 0

    def __str__(self):
        return str(self.heap[1:])
✅ Ejemplo de uso:
python
Copiar código
h = MaxHeap()
h.insertar(10)
h.insertar(4)
h.insertar(15)
h.insertar(20)
h.insertar(3)

print("Heap:", h)
print("Máximo:", h.obtenerMax())

print("Eliminar máximo:", h.eliminarMax())
print("Heap después de eliminar:", h)
