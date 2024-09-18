def saludar(name):
    return f'¡hola {name}, qué tal estás!'

def despedir(name):
    return f'¡Hasta mañana {name}!'

if __name__ == '__main__':
    saludo, despedida = saludar('José'), despedir('José')
    print(saludo + '\n' + despedida)
    