class Actividad1:
    def __init__(self, df):
        self.df = df

    def ejecutar(self):
        print("--------------- ACTIVIDAD 1 --------------------")
        print(self.df.head(2))
        print(self.df.tail(2))
        print(self.df.info())
        print(self.df.describe())

        print("Velocidad Máxima:", self.df["Velocidad_detectada"].max())
        print("Velocidad Mínima:", self.df["Velocidad_detectada"].min())