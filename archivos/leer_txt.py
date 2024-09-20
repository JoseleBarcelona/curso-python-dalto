archivo = open('archivos\\texto.txt', encoding='utf-8') #codificamos a utf-8 para no tener problemas de acentos y caracteres españoles
#LEER ARCHIVO COMPLETO
# leer_archivo = archivo.read()
# print(leer_archivo)
'''
Buenos días, esto es un texto para hacer pruebas de lectura con python
Esta es una segunda linea
Y ahora escribimos la tercera linea

'''
#LEER LINEA POR LINEA
# lineas = archivo.readlines()
# print(lineas)
'''
['Buenos días, esto es un texto para hacer pruebas de lectura con python\n', 'Esta es una segunda linea\n', 'Y ahora escribimos la tercera linea\n']

'''
#LEER UNA SOLA LINEA
# linea = archivo.readline()
# print(linea)
'''
Buenos días, esto es un texto para hacer pruebas de lectura con python

'''
# caracteres = archivo.readline(15)
# print(caracteres)
'''
Buenos días, es

'''
archivo.close() #es muy importante cerrar siempre el archivo cuando se haya usado
