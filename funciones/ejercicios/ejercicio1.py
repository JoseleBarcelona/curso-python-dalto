#Crear una función que pida el nombre y la edad a las personas que vinieron hoy a clase.
#Ordenar los datos de mayor a menor y decir quién el el profesor y quién el asistente.
#Tener en cuenta el asistente es el de menor edad y el profesor el de mayor edad.


#Función para obtener el asistente y el profesor según la edad.
def obtener_clase(numero_de_personas):

    #Creamos una lista vacía para agregar a las personas que componen la clase.
    clase = []

    #Ejecutamos un for para pedir la información de cada persona
    for i in range(numero_de_personas):
        nombre = input("Escriba su nombre: ")
        edad = int(input("Escriba su edad: "))

        #Creamos una tupla con los datos obtenidos.
        datos_alumnos = (nombre, edad)

        #Agregamos los datos obtenidos a la lista.
        clase.append(datos_alumnos)

    #Ordenamos los datos de menor a mayor por la edad.
    clase.sort(key=lambda x: x[1])

    #clase[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre.
    asistente = clase[0][0]
    profesor = clase[-1][0]

    #Retornamos una nueva tupla con el valor de sus variables
    return (asistente, profesor)

#Desempaquetamos la tupla que nos retorna la función, guardándo en cada variable el valor de la tupla por orden.
#El nombre de las variables desmpaquetadas, no tienen porque coincidir con el que retorna la función, pero los 
#hacemos por coherencia y mayor legibilidad
asistente, profesor = obtener_clase(3)

#Mostramos el resultado forzando el orden de los valores con los {valores_que_nos_interese}
print(f'El profesor es {profesor} y el alumno es {asistente}')

'''
Escriba su nombre: José
Escriba su edad: 53
Escriba su nombre: Núria
Escriba su edad: 34
Escriba su nombre: Neus
Escriba su edad: 15
El profesor es José y el alumno es Neus

'''