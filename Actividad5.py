import numpy as np

class Actividad5:
    def __init__(self, df):
        self.df = df

    def ejecutar(self):
        print("--------------- ACTIVIDAD 5 --------------------")

        self.df.loc[2, "Velocidad_detectada"] = np.nan
        print(self.df.loc[0:5])

        print("Nulos:")
        print(self.df.isnull().sum())

        self.df["Velocidad_detectada"] = self.df["Velocidad_detectada"].fillna(1)
        print("Reemplazo:")
        print(self.df.isnull().sum())

        self.df["total_exceso"] = self.df["Velocidad_detectada"] - self.df["Límite_velocidad"]
        print(self.df["total_exceso"].head())
