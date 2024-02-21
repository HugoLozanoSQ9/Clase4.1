car = {
    'brand' :'Ford',
    'model' : 'Mustang',
    'year' : 1964,
}

car['year']=2018 #como ya existe la llave solamente se sustituye el valor
car['color']='blue' #Como no existe simplemente lo va a crear

print(car) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'blue'}

#método update()
car.update({'status':'new', 'year':'2005'})#{'brand': 'Ford', 'model': 'Mustang', 'year': '2005', 'color': 'blue', 'status': 'new'}

print(car)

#Método pop()
#Elimina el elemento con la llave especificada

car.pop('model') #{'brand': 'Ford', 'year': '2005', 'color': 'blue', 'status': 'new'}
print(car) #ya no mostrará ni la llave ni el valor 

#Método popitem()
#El método popitem() elimina el último elemento añadido "(Esto solo aplica en versiones 3.7 y superiores"

car.popitem() #{'brand': 'Ford', 'year': '2005', 'color': 'blue'}
print(car)

#Método fromkeys() indica que podemos crear un nuevo diccionario con ciertas llaves 
#Primer argumento es una lista de llaves, y el segundo argumento es una lista a aplicar
new_car = car.fromkeys(['brand','model'],'Ford') #{'brand': 'Ford', 'model': 'Ford'}
print(new_car)

#Método copy() Básicamente lo que hace es copiar mi diccionario a este momento
car_car = car.copy() #{'brand': 'Ford', 'year': '2005', 'color': 'blue'}

print(car_car)

#método clear() este método vadía el diccionario

car.clear()
print(car) #{ }

#Método setdefault() Devuelve el valor de la llave especificada. Si la llave no existe, inserta la llave con el valor específico
car.setdefault('hola') #{'hola': None}
print(car)
#Método values() Devuelve una lista de todos los valores del diccionario
print(car.values())#dict_values([None])










