with open('archivos\\texto2.txt', 'w', encoding='utf-8') as archivo:
    #SOBRESCRIBIMOS EL ARCHIVO POR COMPLETO PASANDO UNA LISTA
    # archivo.writelines(['Hola chavales\n', 'Qué tal estais!.', ' Espero qué bien.', '\nTodo perfecto'])
    '''
    Hola chavales
    Qué tal estais!. Espero qué bien.
    Todo perfecto
    
    '''
    #SOBRESCRIBIMOS UNA SOLA LINEA POR COMPLETO
    archivo.write('- Hola a todos los compañeros de MCM\n')
    archivo.write('- Hola a todos los compañeros de MCM')
    '''
    
    Hola a todos los compañeros de MCM
    Hola a todos los compañeros de MCM

    '''
