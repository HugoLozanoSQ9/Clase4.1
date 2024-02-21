#Se puede acceder al valor de los elementos, con la nomenglatura llave / clave
car = {
    'brand' :'Ford',
    'model' : 'Mustang',
    'year' : 1964,
}
print(car['model']) #'Mustang'

#######################################
#Método get()
#Es posible utilizar el método get(). 
#Con esto es posible especificar un valor default en caso de que el diccionario no contenga la llave especificada

print(car.get('model')) #Mustang
print(car.get('owner')) #None
print(car.get('owner', 'No owner')) #Si  no existe owner muestra de forma automática el texto 'No owner'

#Método keys() devuelve una lista con todas las llaves del diccionario 

keys = car.keys() #Así solo ingreso a los valores de las llaves si yo hago esto: list(car.keys()) no podré modificar nada pq es 
#una nueva lista

print(keys) #dict_keys(['brand','model','year'])

car['owner'] = 'Alfredo Altamirano'

print(car)
print(keys)


#Yo puedo añadir elementos al diccionario de 2 formas ya sea con 
#car['owner'] = 'Alfredo Altamirano' o con 
#attrs = {'owner':'Alfredo Altamirano', 'color':blue}
#car.update(attrs)

#Método values() que es lo mismo que keys() solo que esta vez con los valores de la lista
values = car.values()
print(values)
#Método items() devuelve cada elemento de un diccionario como tuplas en una lista

items = car.items()
print(items) #dict_items([('brand','Ford'),('model','Mustang'),('year',1964)])

#Operador in en diccionarios permite evaluar si una llave especifica está presente en el diccionario 

print('model' in car) #Esto devueleve un True

if 'model' in car:
    print('la llave model está presente en el diccionario')

    







