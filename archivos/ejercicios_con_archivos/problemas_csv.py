#Camiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv('archivos\\ejercicios_con_archivos\\datos2.csv')
df['Edad'] = df['Edad'].astype(str)
edades = df['Edad']
print(edades)
print(type(edades[0]))
'''
0    54
1    21
2    84
3    12
4    32
5    22
Name: Edad, dtype: object
<class 'str'>

'''
#remplazar el dato de una columna por otro dato
apellido_remplazado = df['Apellido'].replace('López', 'Trancoso')
print(apellido_remplazado)
'''
0    Trancoso
1      García
2    Barranco
3     Durango
4     Alzivar
5     Argarot
Name: Apellido, dtype: object

'''
df2 = pd.read_csv('archivos\\ejercicios_con_archivos\\datos3.csv')
print(df2)
'''
0   Antonio     López  54.0
1     María    García  21.0
2     Laura  Barranco  84.0
3      Leia   Durango  12.0
4   Martina   Alzivar  32.0
5    Steven   Argarot  22.0
6    Steven   Argarot  22.0
7    Steven   Argarot  22.0
8    Steven   Argarot  22.0
9    Steven       NaN   NaN
10   Steven   Argarot   NaN

'''
df2 = pd.read_csv('archivos\\ejercicios_con_archivos\\datos3.csv')
df2 = df.drop_duplicates() #Elimina datos duplicados
print(df2)
'''
    Nombre  Apellido Edad
0  Antonio     López   54
1    María    García   21
2    Laura  Barranco   84
3     Leia   Durango   12
4  Martina   Alzivar   32
5   Steven   Argarot   22

'''
df2 = pd.read_csv('archivos\\ejercicios_con_archivos\\datos3.csv')
print(df2)
'''
0   Antonio     López  54.0
1     María    García  21.0
2     Laura  Barranco  84.0
3      Leia   Durango  12.0
4   Martina   Alzivar  32.0
5    Steven   Argarot  22.0
6    Steven   Argarot  22.0
7    Steven   Argarot  22.0
8    Steven   Argarot  22.0
9    Steven       NaN   NaN
10   Steven   Argarot   NaN

'''
df2 = pd.read_csv('archivos\\ejercicios_con_archivos\\datos3.csv')
df2 = df.dropna() #Elimina datos no disponibles Na (Not Available)
print(df2)
'''
    Nombre  Apellido Edad
0  Antonio     López   54
1    María    García   21
2    Laura  Barranco   84
3     Leia   Durango   12
4  Martina   Alzivar   32
5   Steven   Argarot   22

'''
#Crear un nuevo archivo csv con los datos csv limpios de duplicados y valores no disponibles
df2.to_csv('archivos\\ejercicios_con_archivos\\datos3_limpiados.csv')
print(df2)