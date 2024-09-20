#'a' append agrega texto sin sobrescribir, cada vez qeu se ejecuta el código
with open('archivos\\texto3.txt', 'a', encoding='utf-8') as archivo:
    for i in range(5):
        archivo.write(f'- Archivo {i} agregado\n')

'''
- Archivo 0
- Archivo 1
- Archivo 2
- Archivo 3
- Archivo 4


'''