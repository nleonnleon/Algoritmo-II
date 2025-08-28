my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)

# Reemplazar el valor más bajo por 0
my_array = [10 if i == minVal else i for i in my_array]
print('Nuevo array:', my_array)
