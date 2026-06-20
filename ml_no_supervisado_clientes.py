import pandas as pd
from sklearn.cluster import KMeans

# Configuracion para la visualizacion de filas o columnas del dataset
pd.set_option('display.max_rows', None)

#Cargar el Dataset

df = pd.read_csv('Mall_Customers.csv')
#print(df.head())

# El centro comercial quiere crear un total de tres grupos
# 0 = Clientes ahorradores
# 1 = Clientes regulares
# 2 = Clientes VIP


#Seleccionar las variables a utilizar de nuestro Dataset
# Annual Income (k$)
# Spending Score (1-100)
X = df[[
    'Annual Income (k$)',
    'Spending Score (1-100)'
]]

#print(X)
print('--' * 30)

# Crear el modelo
modelo = KMeans(
    n_clusters = 3,
    random_state=50
)
# Entrenar al modelo
modelo.fit(X)

#Obtener los grupos
grupos = modelo.labels_

#Agregar el grupo a nuestro DataFrame
df['Grupo'] = grupos
print('Agregando el grupo al final del DataFrame:')
print(df.head())
print('--' * 30)

#Asignar nombres a los grupos
nombres_grupos = {
    0: 'Clientes ahorradores',
    1: 'Clientes regulares',
    2: 'Clientes VIP'
}

#Creamos una nueva columna
df['Tipo_cliente'] = df['Grupo'].map(nombres_grupos)
print('DataFrame final logrado')
print(df)

#Nueva prediccion
nuevos_clientes = [
    [70, 20],
    [50, 54],
    [90, 93]
]

predicciones = modelo.predict(nuevos_clientes)
print(predicciones)

#Queremos que en vez de numero entregue la clasificacion
def clasificar_cliente(prediccion):
    if prediccion == 0:
        return 'Cliente ahorrador'
    elif prediccion == 1:
        return 'Cliente regular'
    elif prediccion == 2:
        return 'Cliente VIP'
    else:
        return 'Prediccion desconocida'

for i in range(len(predicciones)):
    print(f'Cliente {i+1}: {clasificar_cliente(predicciones[i])}')

