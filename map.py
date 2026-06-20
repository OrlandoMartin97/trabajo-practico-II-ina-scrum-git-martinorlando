numeros = [1,2,3,4,5]

# Crear la funcion para duplicar
def duplicar(numero):
    return numero * 2

resultado = map(duplicar, numeros)
#print(resultado)

resultadoLista = list(resultado)
print(resultadoLista)

#Otra forma de programar esto en python
resultado_lista = []

for numero in numeros:
    resultado_lista.append(numero * 2)
    
print(resultado_lista)

# Vemos un ejemplo de como se usa el map, pero con pandas
import pandas as pd

df = pd.DataFrame({
    'grupos' : [0,1,0,2]
})

# Diccionario de nombres de grupos
nombres = {
    0 : 'GRUPO A',
    1 : 'GRUPO B',
    2 : 'GRUPO C'
}

# Agregar una nueva columna de nombres de grupo a nuestro DataFrame
df['nombre_grupo'] = df['grupos'].map(nombres)

print(df)
#Creamos el archivo CSV
df.to_csv('grupos.csv', index=False)
