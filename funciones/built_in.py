numeros = [8,7,3,98,67,45,13,105,54,78]

#Buscar el número más alto de una lista
numero_mas_alto = max(numeros)
print(f'El número más alto de la lista es {numero_mas_alto}') #105

#Buscar el número más bajo de una lista
numero_mas_bajo = min(numeros)
print('El número más bajo de la lista es {}'.format(numero_mas_bajo)) #3
print('El número más bajo es {} y el más alto es {}'.format(numero_mas_bajo, numero_mas_alto))

#Redondear un número con x decimales dados por parámetro
numero = 18.698536698725648
print(f'El número redondeado con tres decimales es {round(numero,3)}') #18.698

#Retorna False -> False, 0, vacio, None \ True -> distinto a 0, True, cadena , datos no vacios
print(bool(False)) #False
print(bool(0)) #False
print(bool([])) #False
print(bool(None)) #False
print(bool(5)) #True
print(bool(True)) #True
print(bool('hola')) #True
print(bool(('hola', 7))) #True

#Hace lo mismo que bool() pero con un elemento iterable
lista1 = all([True, 84, 'hola', [58, True]])
lista2 = all([None, 84, 'hola', [58, True]])
print(lista1) #True
print(lista2) #False

#Suma todos los valores de un iterable
print(sum(numeros)) #478

