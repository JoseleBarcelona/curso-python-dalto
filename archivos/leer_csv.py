import csv

with open('archivos\\datos.csv', 'r', encoding='utf-8') as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)

'''
['nombre', 'apellido', 'nombre']
['Antonio', 'López', '54']
['María', 'García', '21']
['Laura', 'Barranco', '84']

'''
