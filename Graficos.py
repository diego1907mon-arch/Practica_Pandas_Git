import matplotlib.pyplot as plt

class Graficos:
    def __init__(self, df):
        self.df = df

    
    def grafico_1_barra(self):
        print("--- GRÁFICO: EXCESO TOTAL POR MARCA ---")

        total_marca = self.df.groupby("Marca_vehículo")["total_exceso"].sum()

        total_marca.plot(kind="bar", title="Exceso total por marca")
        plt.xlabel("Marca")
        plt.ylabel("Total exceso")
        plt.show()

 
    def grafico_2_circular(self):
        print("--- GRÁFICO: EXCESO POR TIPO DE VÍA ---")

        total_via = self.df.groupby("Tipo_vía")["total_exceso"].sum()

        total_via.plot(kind="pie", autopct="%1.1f%%", title="Exceso por tipo de vía")
        plt.ylabel("")
        plt.show()


    def grafico_3_histograma(self):
        print("--- HISTOGRAMA: VELOCIDAD DETECTADA ---")
        plt.hist(self.df["Velocidad_detectada"], bins=10)
        plt.title("Histograma de velocidades")
        plt.xlabel("Velocidad")
        plt.ylabel("Frecuencia")
        plt.show()