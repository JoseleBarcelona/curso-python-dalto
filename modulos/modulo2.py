import modulos_saludar as sl

#Asignamos un alias para facilitar el código y evitar conflictos entre nombres de variables y funciones.
saludo = sl.saludar('Núria') 
despedida = sl.despedir('Núria')
print(saludo + '\n' + despedida)

print(sl.__name__)
print(__name__)