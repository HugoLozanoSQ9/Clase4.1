# Continuación de la clase 4

## List Comprehension 

python ofrece una sintaxis más corta cuando necesitas crear una nueva lista basada en los valores de otra lista preexistente

nueva_lista = [expresión for elemento in iterable if condicion]

## Diccionarios

Se utilizan para almacenar datos en pares de tipo clave - valor (key - value)

Es una colección de datos ordenada*, modificable y que no admite duplicados 
"( LOs dicionarios son ordenados a partir de python 3.7)"
Ordenadas  --> se refiere a que los elementos tienen un orden definido y que ese orden no cambiará
Modificables --> Es posible cambiar, añadir y remover elementos después de haber sido declaradas
No duplicados --> Un diccionario no puede tener 2 elementos con la misma llave

## Tuplas

Se utilizan para almacenar múltiples elementos en una sola variable
Son ordenadas, permiten valroes duplicados y inmutables

Ordenadas -> Orden definido y ese orden no cambia
Permiten duplicados -> Al ser indexadas (como las listas) pueden tener elementos con el mismo valor
Inmutables -> no podemos añador, modificar ni eliminar elementos una vez que la tupla ha sido declarada

## Sets

Los sets se utilizan para almacenar múltiples elementos en una sola variable
Es una colección de datos desordenada, inmutable "a medias" y no indexada 
(no se pueden modificar, si se pueden añadir nuevs elementos y eliminar)

Desordenadas-> No tienen un orden definido, los elementos pueden aparecer en un orden diferente cada vez que se utilicen 
No se pueden referenciar por medio de un índice o llave

Inmutables -> No podemos modificar los elementos después de haber declarado el set
Sin embargo, es posible adicionar y eliminar elementos

No permiten duplicados -> Los sets no pueden tener elementos con el mismo valor

Se suelen utilizar refiriendose a la teoría de conjuntos (prácticamente son la intersección de 2 conjuntos)

