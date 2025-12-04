import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("dataset_fotomultas_1000.csv")



print("---------------ACTIVIDAD 1--------------------")


print("----------------------------")
print(df.head(2)) 
print("----------------------------")
print(df.tail(2)) 
print("----------------------------")
print(df.info()) 
print("----------------------------")
print(df.describe()) 
print("----------------------------")
print('velocidad maxima')
print(df["Velocidad_detectada"].max())
print('velocidad minima')
print(df["Velocidad_detectada"].min())




print("---------------ACTIVIDAD 2--------------------")


print(df["Hora"])                      
print(df[["Marca_vehículo", "Placa"]])
print(df.iloc[0:3]) 


print(df[df['Marca_vehículo']=='BMW'])
print(df[df['Velocidad_detectada']>50])



print(df[df["Tipo_vía"] == "Autopista"].shape[0])

print(df[df["Velocidad_detectada"] > 100].shape[0])

print("---------------ACTIVIDAD 3--------------------")

df["Superó_límite"] = df["Velocidad_detectada"] > df["Límite_velocidad"]

print(df[
    [
        'ID_foto',
        'ID_cámara',
        'Velocidad_detectada',
        'Límite_velocidad',
        'Hora',
        'Clima',
        'Tipo_vía',
        'Marca_vehículo',
        'Placa',
        'Cámara_funcionaba',
        'Superó_límite'
    ]
])



df["total_exceso"] = df["Velocidad_detectada"] - df["Límite_velocidad"]
print("Valor más alto en total:", df["total_exceso"].max())


print("---------------ACTIVIDAD 4--------------------")

ordenar_exceso=df.sort_values('total_exceso',ascending=False)
print(ordenar_exceso)




total_por_marca = df.groupby("Marca_vehículo")["total_exceso"].sum()
print("Total vendido por (Marca_vehículo):")
print(total_por_marca)


total_por_via = df.groupby("Tipo_vía")["total_exceso"].sum()
print("Total por (Tipo_vía):")
print(total_por_via)




# 4A. ¿Qué producto (Marca_vehículo) genera más total?

marca_max = total_por_marca.idxmax()
valor_marca_max = total_por_marca.max()

print("Marca del vehìculo con más exceso de velocidad:", marca_max)
print("Valor generado:", valor_marca_max)



via_max = total_por_via.idxmax()
valor_via_max = total_por_via.max()

print("Tipo_vía que aporta mayor exceso de velocidad:", via_max)
print("Valor generado:", valor_via_max)



print("---------------ACTIVIDAD 5--------------------")

df.loc[2, "Velocidad_detectada"] = np.nan
print(df.loc[0:5])


print(df.isnull().sum())

df["Velocidad_detectada"] = df["Velocidad_detectada"].fillna(1)

print(df.isnull().sum())

df["total_exceso"] = df["Velocidad_detectada"] - df["Límite_velocidad"]
print( df["total_exceso"])



print("---------------ACTIVIDAD 6--------------------")


fig,axes=plt.subplots(2,1,figsize=(8,8))