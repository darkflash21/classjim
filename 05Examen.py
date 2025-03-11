import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el archivo CSV
df = pd.read_csv('./housing.csv')
columnas = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']

# Función para calcular medidas estadísticas
def calcular_estadisticas(serie):
    serie = pd.Series(serie)
    return pd.DataFrame({
        'Media': [serie.mean()],
        'Mediana': [serie.median()],
        'Moda': [serie.mode().iloc[0]],
        'Desviación Estándar': [serie.std()],
        'Rango': [serie.max() - serie.min()],
        'Varianza': [serie.var()]
    })

# Imprimir medidas estadísticas de cada columna
for columna in columnas:
    print(f"Estadísticas para la columna: {columna}\n", calcular_estadisticas(df[columna]), "\n")

# Graficar relación entre población y precio de vivienda
plt.bar(df['population'][:10000], df['median_house_value'][:10000], width=500)
plt.xlabel('Población')
plt.ylabel('Valor medio de la vivienda')
plt.title('Relación entre población y precio de la vivienda')
plt.show()
