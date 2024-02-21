#Tuplas
tupla = (1,3,5,8,9,6,8,1,3)
#for i in tupla: #Se puede iterar
    #print (i) #1,3

print(tupla.count(3)) #Cuenta cuantas veces aparece un valor especificado ->2
 
print(tupla.index(8)) #evuelve el índice de un valor especificado --> 3 

#Si se declara una tupla con un solo elemento entonces sería como si tuviera una variable, excepto si se pone una ',' al declararla

fruits2 = ('banana') #--> esto es un str (un string)

fruits1 = ('Cherry',) #--> esto es una tupla

fruits = ('banana','apple','cherry')

(fruit1,fruit2,fruit3)=fruits #Unpacking (sería como desempaquetar las tuplas)

print(fruits1,fruit2,fruit3) #Me permite sacar los valores de fruit por variable  

contador = 0

for i in tupla:
    contador += 1
    print(i,contador)
 #Se pueden mezclar como las listas tupla_final = tupla1 + tupla2
    
    
