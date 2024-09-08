#forma no óptima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados += numero
    return numeros_sumados

resultado = suma([3,8,6,9,10])
print(resultado)

#Forma óptima de sumar valores
def suma2(*lista):
    return sum(lista)

resultado = suma2(3,8,6,9,10)
print(resultado)

#Otra forma de sumar valores, pasando varios parámetros
def suma3(nombre, *lista): #El * tiene que ir siempre en el último lugar de los parámetros
    return f'Me llamo {nombre} y mi operación suma {sum(lista)}'

resultado = suma3('Antonio',3,8,6,9,10)
print(resultado)

#Otra forma de sumar valores pasando el parámetro args en una función built-in
def suma4(lista):
    return sum([*lista])

resultado = suma4([3,8,6,9,10])
print(resultado)