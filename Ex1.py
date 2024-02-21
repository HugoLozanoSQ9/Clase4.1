#Escribir un script que permita ordenar la siguiente lista de tuplas por el segundo valor de cada tupla
#de manera ascendente y descendente

pair_numbers= [(2,5),(1,2),(4,4),(2,3),(2,1)]

#[(2,1),(1,2),(2,3),(4,4)]
#[(4, 4), (2, 3), (2, 3), (2, 1), (1, 2)]
"""
def get_second_value(tupla): #obten el segundo valor de cada tupla
    return tupla[1]

pair_numbers.sort(key=get_second_value)
print('Orden ascendente:', pair_numbers)
pair_numbers.sort(reverse = True)
print('Orden descendente:', pair_numbers)

"""



