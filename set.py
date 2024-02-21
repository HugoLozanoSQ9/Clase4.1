# Casi no se ocupan a menos de que nos dediquemos al computo enfocado a ciencias o para generar un iterador no repetido
# por decir tener 10 números repetidos --> pasarlos a un set y ahora solo tener 1 numero
"""
Métodos de los sets

add() Añade un elemento
clear() Elimina todos los elementos del set
copy() Devuelve una copia del set
differece() Devuelve un ser que contiene la diferencia entre 2 o más sets
difference_update() Elimina los elementos en este set que también están incluidos en otro set especificado 
discard() Elimina el elemento especificado
intersection() Devuelve un set que contiene la intersección de otros 2 sets
intersection_update() Elimina los elementos en este set que no están presente en otro(s) set(s) especificado(s)
isdisjoint() Devuelve si es que 2 sets tienen una intersección o no 
issubset() Devuelve si es que otro set contiene este set o no
issuperset() Devuelve si este set contiene otro set o no 
pop() Elimina un elemento del set
remove()Elimina en elemento especificado 
symmetric_difference() Devuelve un set con las diferencias simetricas de 2 sets
symmetric_difference_update() Inserta las diferncias simétricas de 2 sets
union() Devuelve un set con la union de 2 sets
update() Actualiza el set con la union de 2 o más sets.

"""
sets = {1,2,3}

sets.add(9)
other_set = sets.copy()
print(other_set)
print(sets)
