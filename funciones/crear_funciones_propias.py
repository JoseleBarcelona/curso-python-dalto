#Función simple
def saludar():
    print('¡Hola qué tal!')

saludar() #¡Hola qué tal!

#Función con parámetros
def saludo(nombre, sexo):
    sexo = sexo.lower()
    if sexo == 'hombre':
        adjetivo = 'chaval'
    elif sexo == 'mujer':
        adjetivo = 'señorita'
    else:
        adjetivo = 'amor'
    print(f'hola {nombre} mi {adjetivo}')

saludo('Antonio', 'Hombre') #hola Antonio mi chaval
saludo('Laura', 'MUJER') #hola Laura mi señorita
saludo('Elle', 'no_binario') #hola Elle mi amor

#Función que retorna valores
def crear_contraseña_random(num):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num + 2
    c2 = num
    c3 = num -5
    return f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    
password = crear_contraseña_random(158) #dbw2
print(password)
