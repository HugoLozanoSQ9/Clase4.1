# Python ofrece una sintaxis más corta cuando necesitas crear un nuevo diccionario basada en los valores de otro iterable
# nuevo_diccionario = {llave:valor for elemento in iterable if condicion}
#Forma tradicional de hacerlo 
"""
def celcius_to_fahrenheit(value) -> float:
    return (value * 9 / 5) + 32


celcius_presets = {"L1": 18, "L2": 20, "L3": 22, "L4": 23}

fahrenheit_presets = {}

for level,value in celcius_presets.items():
    fahrenheit_presets[level] = celcius_to_fahrenheit(value)

print(celcius_presets) #{'L1': 18, 'L2': 20, 'L3': 22, 'L4': 23}
print(fahrenheit_presets) #{'L1': 64.4, 'L2': 68.0, 'L3': 71.6, 'L4': 73.4}
"""

#Con dictionary comprehension

def celcius_to_fahrenheit(value) -> float:
    return (value * 9 / 5) + 32

celcius_presets = {"L1": 18, "L2": 20, "L3": 22, "L4": 23}

fahrenheit_presets = {key.lower():celcius_to_fahrenheit(v) for key,v in celcius_presets.items()}

print(celcius_presets) #{'L1': 18, 'L2': 20, 'L3': 22, 'L4': 23}
print(fahrenheit_presets) #{'L1': 64.4, 'L2': 68.0, 'L3': 71.6, 'L4': 73.4}

