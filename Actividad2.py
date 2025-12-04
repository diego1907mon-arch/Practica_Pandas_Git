class Actividad2:
    def _init_(self, df):
        self.df = df

    def ejecutar(self):
        print("--------------- ACTIVIDAD 2 --------------------")

        print(self.df["Hora"])
        print(self.df[["Marca_vehículo", "Placa"]])
        print(self.df.iloc[0:3])

        print(self.df[self.df["Marca_vehículo"] == "BMW"])
        print(self.df[self.df["Velocidad_detectada"] > 50])

        print("Cantidad Autopista:", self.df[self.df["Tipo_vía"] == "Autopista"].shape[0])
        print("Velocidad > 100:", self.df[self.df["Velocidad_detectada"] > 100].shape[0])
        