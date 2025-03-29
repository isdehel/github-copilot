import pandas as pd
import matplotlib.pyplot as plt
import os

# Verificar si el archivo existe
archivo = 'data.xlsx'

if not os.path.exists(archivo):
    print(f"Error: El archivo {archivo} no existe.")
else:
    # Cargar el archivo Excel
    df = pd.read_excel(archivo)

    # Suponiendo que el campo de horas se llama 'Horas'
    horas = df['Horas']

    # Generar la tendencia de consumo
    plt.plot(horas)
    plt.title('Tendencia de Consumo')
    plt.xlabel('Tiempo')
    plt.ylabel('Consumo')
    plt.show()
