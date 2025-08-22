pilaFia = []
pilaFia2 = []

# Push inicial
pilaFia.append(1)
pilaFia.append(2)
pilaFia.append(3)
pilaFia.append(4)
pilaFia.append(5)
pilaFia.append(6)
pilaFia.append(7)

print("Pila inicial:", pilaFia)

sacarD = 5
temp = 0

# Sacar elementos hasta encontrar el número deseado
while pilaFia:
    temp = pilaFia.pop()
    if temp == sacarD:
        print(f"¡Número {sacarD} eliminado!")
        break
    else:
        pilaFia2.append(temp)

print("Pila después de eliminar el número:", pilaFia)
print("Elementos guardados temporalmente:", pilaFia2)

# Restaurar los elementos en el orden original
while pilaFia2:
    pilaFia.append(pilaFia2.pop())

print("Pila restaurada (sin el número eliminado):", pilaFia)