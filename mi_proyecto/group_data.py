import pandas as pd
import os

def leer_excel(ruta_archivo):
    """
    Lee un fichero Excel y devuelve un DataFrame de pandas.
    
    :param ruta_archivo: Ruta del fichero Excel.
    :return: DataFrame con los datos del fichero Excel.
    """
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe.")
        return None
    return pd.read_excel(ruta_archivo)

# Cargar el archivo Excel usando la nueva función
archivo = 'data.xlsx'
df = leer_excel(archivo)

if df is not None:
    # Filtrar filas donde el campo 'aceptación' está informado
    df_filtrado = df[df['Aceptación QA'].notna()]

    # Agrupar por 'grupo', 'dominio funcional' y 'aceptación'
    df_agrupado = df_filtrado.groupby(['Grupo', 'Area', 'Aceptación QA']).size().reset_index(name='conteo')

    # Mostrar el resultado
    print(df_agrupado)