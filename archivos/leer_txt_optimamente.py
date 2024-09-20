#Con with open nos olvidamos de tener que cerrar el archivo, ya que lo hace automáticamente
with open('archivos\\texto.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print(contenido)
'''
Buenos días, esto es un texto para hacer pruebas de lectura con python
Esta es una segunda linea
Y ahora escribimos la tercera linea

'''