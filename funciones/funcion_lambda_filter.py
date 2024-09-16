numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#función filter usando una función simple

def es_par(num):
    if num %2 == 0:
        return True
    
numeros_pares = filter(es_par, numeros) #filter retorna los elementos que sean True de la función que le pasamos
print(list(numeros_pares)) #[2, 4, 6, 8, 10, 12]

#función filter usando una función anónima lambda

numeros_pares_lambda = filter(lambda x: x %2 == 0, numeros)
print(list(numeros_pares_lambda)) #[2, 4, 6, 8, 10, 12]
