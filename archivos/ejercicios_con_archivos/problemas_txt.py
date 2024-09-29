nombres = ['Antonio', 'María', 'Carla', 'Raúl', 'Laura']
apellidos = ['García', 'Rodriguez','Alvarez', 'Sanchez','Guerra']
edades = [54, 68, 14, 26, 34]

with open('archivos\\ejercicios_con_archivos\\datos.txt', 'w', encoding='utf-8') as datos:
    datos.write('Datos de los alumnos:\n\n')
    for n, a, e in zip(nombres, apellidos, edades):
        datos.write(f'Nombre: {n}\nApellido: {a}\nEdad: {e}\n----------\n')
    # [datos.write(f'Nombre: {n}\nApellido: {a}\nEdad: {e}\n----------\n')  for n, a, e in zip(nombres,apellidos, edades)]

'''
Datos de los alumnos:

Nombre: Antonio
Apellido: García
Edad: 54
----------
Nombre: María
Apellido: Rodriguez
Edad: 68
----------
Nombre: Carla
Apellido: Alvarez
Edad: 14
----------
Nombre: Raúl
Apellido: Sanchez
Edad: 26
----------
Nombre: Laura
Apellido: Guerra
Edad: 34
----------


'''