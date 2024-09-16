#Escribe una función que dándole un parámetro, cree la secuencia de fibonacci hasta el parámetro dado

def secuencia_fibonacci(number):
    a,b=0,1 #desempaquetamos
    lista_fibonacci = [0]
    for i in range(number):
        if b > number: return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a,b = b, a+b

resultado = secuencia_fibonacci(54)
print(resultado)