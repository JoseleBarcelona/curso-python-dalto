#función multiplicar por 2 sin función lambda

def multiplicar_por_dos(x):
    return x*2
print(multiplicar_por_dos(4)) #8

#función multiplicar por 2 con función lambda
#Las funciones lambda retornan directamente sin necesidad de hacer un return

multiplicar_lambda = lambda x: x*2 #
print(multiplicar_lambda(4)) #8

#función simple para efectuar una simple ecuación

def ecuacion(x,y):
    return (x+y)/2 + (x**2)
print(ecuacion(2,4)) #7.0

#función lambda para efectuar una simple ecuación
ecuacion_lambda = lambda x, y: (x+y)/2 + (x**2)
print(ecuacion_lambda(2,4)) #7.0
