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

 