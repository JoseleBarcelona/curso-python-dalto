from modulos_saludar import saludar, despedir

#Importamos los métodos que vamos a utilizar, pudiendo llamalos directamente sin poner modulos_saludar.saludar()
saludo = saludar('Núria') 
despedida = despedir('Núria')
print(saludo + '\n' + despedida)
