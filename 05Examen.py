import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Función para calcular estadísticas de notas
def estadisticas_notas(notas):
    estadistica = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], 
                            index=['MIN', 'MAX', 'MEDIA', 'DESVIACION ESTANDAR'])
    return estadistica

# Carga de datos (ajusta la ruta si es necesario)
try:
    df = pd.read_csv("housing.csv")  # Asegúrate de que este archivo esté en la misma carpeta
except FileNotFoundError:
    print("Error: No se encontró el archivo 'housing.csv'. Verifica la ruta.")
    exit()

# Cálculo de estadísticas
media = df['median_house_value'].mean()
mediana = df['median_house_value'].median()
moda = df['median_house_value'].mode()[0]
rango = df['median_house_value'].max() - df['median_house_value'].min()
varianza = df['median_house_value'].var()
desviacion = df['median_house_value'].std()

# Imprimir estadísticas
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Rango: {rango}")
print(f"Varianza: {varianza}")
print(f"Desviación estándar: {desviacion}")

# Tabla de frecuencias
frecuencia = df['median_house_value'].value_counts().reset_index()
frecuencia.columns = ['median_house_value', 'Frecuencia']
print("\nTabla de Frecuencias:")
print(frecuencia.head(10))  # Muestra las primeras 10 filas

# Gráfico de barras corregido
plt.figure(figsize=(10, 6))
sns.barplot(x='population', y='median_house_value', data=df, alpha=0.7)
plt.xlabel("Población")
plt.ylabel("Valor Medio de la Vivienda")
plt.title("Relación entre Población y Precio Medio de Vivienda")
plt.xticks(rotation=45)
plt.show()
