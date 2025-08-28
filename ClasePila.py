class PilaFia:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Pila está vacía"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Pila está vacía"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)
  
  # Creaando una pila de libros 
miPilaLibros = PilaFia()

miPilaLibros.push('Fluent Python')
miPilaLibros.push('Think Python')
miPilaLibros.push('Python a fondo')

print("Pila: ", miPilaLibros.stack)
print("Saco el libro que ingresó al último: ", miPilaLibros.pop())
print("Pila despues de sacar el ultimo libro: ", miPilaLibros.stack)
print("Nuevo elemento superior : ", miPilaLibros.peek())
print("Está vacía la pila?: ", miPilaLibros.isEmpty())
print("Tamaño: ", miPilaLibros.size())