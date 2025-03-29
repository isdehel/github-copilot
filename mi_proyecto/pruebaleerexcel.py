import pandas as pd
import datetime 
import pytz 
#pytz.all_timezones ---> Escribe en consola este comando y aparecerán las 
#                       distintas timezones del mundo, elige la de tu situación.

df = pd.read_excel('data.xlsx', header=None,
                   sheet_name='Hoja1', skiprows=1,)

print(df)
lectura = []

mi_hora = datetime.datetime.now(pytz.timezone('America/Guayaquil')) 

for i in df:
    lectura.append([df.values[i][0], df.values[i][1], df.values[i][2], df.values[i][3]])

# Extraccion de variables:
    contenedor = lectura[i][0]
    fecha = lectura[i][1]
    mercancia = lectura[i][2]
    importadora = lectura[i][3]