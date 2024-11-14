"""
Write a function that takes in a non-empty array of integers sorted in ascending order and returns a
new array of the same length with the squares of the original integers also sorted in ascending
order. If the output number is out of the range [0, SS] (for S=6 the range will be [0, 66]), you will
delete it of the output array. Please, don’t use built-in sort of your language.
Examples with S=6:
> {"array": [1, 2, 3, 5, 6, 8, 9]} -> [1, 4, 9, 25, 36, 64]
> {"array": [-2, -1]} -> [1, 4]
> {"array": [-6, -5, 0, 5, 6]} -> [0, 25, 25, 36, 36]
> {"array": [-10, 10]} -> []


def busqueda(s, number_list):
    rango_max = (s*10)+s
    new_list = [x*x for x in number_list if (x*x) <= rango_max]
    print(new_list)
"""

def square_result (s, number_list):
    max_range = (s*10)+s #calculo el rango maximo
    size = len(number_list) #Tamaño del arreglo

    if size == 0: #Si el arreglo esta vacio, termina el programa.
        return []

    squared_list = [0]*size #Creo un nuevo arreglo con el tamaño del original con 0 en todas las posiciones.
    index = 0
    left = 0
    right = size-1

    while left <= right: #mientras izq sea menor a derecha
        #Calculo los cuadrados de los dos extremos del arreglo.
        left_square = number_list[left]**2
        right_square = number_list[right]**2

        if left_square <= right_square:
            if right_square < max_range:
                squared_list[index]=right_square #agrego el termino a la nueva lista en base a la posision del index
                index+=1
            right -=1 #Como añadí el valor de la derecha me muevo a la izq con este valor
        else:
            if left_square < max_range:
                squared_list[index] = left_square
                index += 1
            left += 1 #Como añadi el valor de la izq muevo este puntero a la derecha.
    print(f"El rango maximo manejado en este ejercicio fue de: [0 , {max_range}]")
    print(f"La lista original contenia: {number_list}")
    print(f"La lista resultante luego de ser procesada es: {squared_list[:index][::-1]}") #dado que puede que el arreglo nuevo sea mas pequeño imprimo hasta index
