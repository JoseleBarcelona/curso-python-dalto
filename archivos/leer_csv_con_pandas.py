import pandas as pd

#df es dataframe
# df = pd.read_csv('archivos\\datos.csv')
# print(df)
'''
    Nombre  Apellido  Edad
0  Antonio     López    54
1    María    García    21
2    Laura  Barranco    84

'''

# df = pd.read_csv('archivos\\datos.csv')
# nombres = df['Nombre']
# print(nombres)
'''
0    Antonio
1      María
2      Laura
Name: Nombre, dtype: object

'''
# df = pd.read_csv('archivos\\datos.csv')
# edad = df['Edad']
# print(edad)
'''
0    54
1    21
2    84
Name: Edad, dtype: int64

'''
# df = pd.read_csv('archivos\\datos.csv',names=['Name','Lastname','Age'])
# print(df)
'''
    Name  Lastname   Age
0   Nombre  Apellido  Edad
1  Antonio     López    54
2    María    García    21
3    Laura  Barranco    84

'''
# df = pd.read_csv('archivos\\datos.csv')
# df_ordenado_ascendente = df.sort_values(by='Edad', ascending=True)
# print(df_ordenado_ascendente)
'''
    Nombre  Apellido  Edad
1    María    García    21
0  Antonio     López    54
2    Laura  Barranco    84

'''
# df = pd.read_csv('archivos\\datos.csv')
# df_ordenado_descendente = df.sort_values(by='Edad', ascending=False)
# print(df_ordenado_descendente)
'''
    Nombre  Apellido  Edad
2    Laura  Barranco    84
0  Antonio     López    54
1    María    García    21

'''
# df = pd.read_csv('archivos\\datos.csv')
# df2 = pd.read_csv('archivos\\datos.csv')
# df_concatenado = pd.concat([df,df2])
# print(df_concatenado)
'''
    Nombre  Apellido  Edad
0  Antonio     López    54
1    María    García    21
2    Laura  Barranco    84
0  Antonio     López    54
1    María    García    21
2    Laura  Barranco    84

'''
# df = pd.read_csv('archivos\\datos.csv')
# primeras_filas = df.head(0)
# print(primeras_filas)
'''
Empty DataFrame
Columns: [Nombre, Apellido, Edad]
Index: []

'''
# df = pd.read_csv('archivos\\datos.csv')
# primeras_filas = df.head(1)
# print(primeras_filas)
'''
    Nombre Apellido  Edad
0  Antonio    López    54

'''
# df = pd.read_csv('archivos\\datos.csv')
# ultimas_filas = df.tail(1)
# print(ultimas_filas)
'''
Nombre  Apellido  Edad
2  Laura  Barranco    84

'''
# df = pd.read_csv('archivos\\datos.csv')
# filas_y_columnas_totales = df.shape
# print(filas_y_columnas_totales)
'''
(3, 3) devuelve una tupla

'''
# df = pd.read_csv('archivos\\datos.csv')
# filas_y_columnas_totales = df.shape
# print(filas_y_columnas_totales[0], filas_y_columnas_totales[1])
'''
3 3

'''
# df = pd.read_csv('archivos\\datos.csv')
# filas_totales, columnas_totales = df.shape
# print(filas_totales, columnas_totales)
'''
3 3

'''
# df = pd.read_csv('archivos\\datos.csv')
# df_info = df.describe()
# print(df_info)
'''
            Edad
count   3.000000
mean   53.000000
std    31.511903
min    21.000000
25%    37.500000
50%    54.000000
75%    69.000000
max    84.000000

'''
# df = pd.read_csv('archivos\\datos.csv')
# elemento_especifico_loc = df.loc[0]
# print(elemento_especifico_loc)
'''
Nombre      Antonio
Apellido      López
Edad             54
Name: 0, dtype: object

'''
# df = pd.read_csv('archivos\\datos.csv')
# elemento_especifico_loc = df.loc[1]
# print(elemento_especifico_loc)
'''
Nombre       María
Apellido    García
Edad            21
Name: 1, dtype: object

'''
# df = pd.read_csv('archivos\\datos.csv')
# elemento_especifico_loc = df.loc[1, 'Nombre']
# print(elemento_especifico_loc)
'''
María

'''
# df = pd.read_csv('archivos\\datos.csv')
# elemento_especifico_loc = df.iloc[1, 0]
# print(elemento_especifico_loc)
'''
María

'''
# df = pd.read_csv('archivos\\datos.csv')
# elemento_especifico_loc = df.iloc[:, 0]
# print(elemento_especifico_loc)
'''
0    Antonio
1      María
2      Laura
Name: Nombre, dtype: object

'''
# df = pd.read_csv('archivos\\datos.csv')
# elemento_especifico_loc = df.iloc[:,1]
# print(elemento_especifico_loc)
'''
0       López
1      García
2    Barranco
Name: Apellido, dtype: object

'''
# df = pd.read_csv('archivos\\datos.csv')
# elemento_especifico_loc = df.iloc[:1]
# print(elemento_especifico_loc)
'''
    Nombre Apellido  Edad
0  Antonio    López    54

'''
# df = pd.read_csv('archivos\\datos.csv')
# elemento_especifico_loc = df.loc[2:]
# print(elemento_especifico_loc)
'''
    Nombre  Apellido  Edad
2  Laura  Barranco    84

'''
# df = pd.read_csv('archivos\\datos.csv')
# elemento_especifico_loc = df.loc[2,:]
# print(elemento_especifico_loc)
'''
Nombre         Laura
Apellido    Barranco
Edad              84
Name: 2, dtype: object

'''
df = pd.read_csv('archivos\\datos.csv')
mayores_de_30_años = df.loc[df['Edad']>30,:]
print(mayores_de_30_años)
'''
    Nombre  Apellido  Edad
0  Antonio     López    54
2    Laura  Barranco    84

'''