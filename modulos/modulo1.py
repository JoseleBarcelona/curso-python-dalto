import modulos_saludar

#Tenemos que llamar a los métodos a través del punto, nombrando al módulo que los contiene, que actua como un objeto.
saludo = modulos_saludar.saludar('Núria' + ' preciosa') 
despedida = modulos_saludar.despedir('Núria')
print(saludo + '\n' + despedida)
