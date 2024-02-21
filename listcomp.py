# Crear una lista de números pares y una lista de númers impares a partir de una lista de números predefinida
"""
Forma tradicional 

numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers =  []
even_numbers = []

for number in numbers:
    if number % 2:
        odd_numbers.append(number)
    else: 
        even_numbers.append(number)
    
print(odd_numbers)
print(even_numbers)
"""

###############################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n practicamente sería number (asimilado alejemplo de arriba)
odd_numbers = [number for number in numbers if number % 2]

# n = expresion o valor que voy a guardar en la nueva lista n = cada elemento de la lista  numbers = iterable  if --> condición (opcional)
# Si no se cumple la condición se salta al siguiente elemento
even_numbers = [number for number in numbers if not number % 2]

print(odd_numbers)
print(even_numbers)
