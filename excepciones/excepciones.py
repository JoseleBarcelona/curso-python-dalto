def sumar_dos():
    while True:
        try:
            a = input('Introduce un número entero: ')
            b = input('Introduce un segundo número entero: ')
            resultado = int(a) + int(b)
        except Exception as e:
            print(f'Tiene una excepción del tipo {type(e)}')
            print(f'Datos de la excepción {e}')
            print({e})
            print('Debes introducir un número entero, vuelva a intentarlo')
        else:
            break
        finally:
            print('CALCULADORA PARA SUMAR DOS PARÁMETROS')

    return f'El resultado de la suma es: {resultado}'

print(sumar_dos())
'''
Introduce un número entero: 8
Introduce un segundo número entero: K
Tiene una excepción del tipo <class 'ValueError'>
Datos de la excepción invalid literal for int() with base 10: 'K'
{ValueError("invalid literal for int() with base 10: 'K'")}
Debes introducir un número entero, vuelva a intentarlo
CALCULADORA PARA SUMAR DOS PARÁMETROS
Introduce un número entero: 10
Introduce un segundo número entero: 5
CALCULADORA PARA SUMAR DOS PARÁMETROS
El resultado de la suma es: 15

'''