fruits = ["banana", "orage", "kiwi", "Melon",1,20, 8.7, "Cherry", 'mango', 'apple'] 

str_fruits = [fruit.upper().replace("A","@") for fruit in fruits if isinstance(fruit, str)] 


print(fruits)
print(str_fruits)