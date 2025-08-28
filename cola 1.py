colaFia = []

# encolar
colaFia.append('A')
colaFia.append('B')
colaFia.append('C')
print("Queue: ", colaFia)

# mostrar el primer elemento
frontElement = colaFia[0]
print("Peek: ", frontElement)

# sacar elemento de la cola
poppedElement = colaFia.pop(0)
print("quitar elemento de la cola: ", poppedElement)

print("cola despues de quitar elemento de la cola: ", colaFia)

# esta vacia?
isEmpty = not bool(colaFia)
print("está vacía: ", isEmpty)

# tamaño de la cola
print("Size: ", len(colaFia))