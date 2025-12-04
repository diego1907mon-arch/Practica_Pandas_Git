class Actividad3:
    def __init__(self, df):
        self.df = df

    def ejecutar(self):
        print("--------------- ACTIVIDAD 3 --------------------")

        self.df["Superó_límite"] = self.df["Velocidad_detectada"] > self.df["Límite_velocidad"]

        print(self.df[[
            'ID_foto', 'ID_cámara', 'Velocidad_detectada',
            'Límite_velocidad', 'Hora', 'Clima', 'Tipo_vía',
            'Marca_vehículo', 'Placa', 'Cámara_funcionaba',
            'Superó_límite'
        ]])

        self.df["total_exceso"] = self.df["Velocidad_detectada"] - self.df["Límite_velocidad"]
        print("Máximo exceso:", self.df["total_exceso"].max())
