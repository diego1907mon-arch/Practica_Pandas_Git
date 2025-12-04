import pandas as pd

class Cargar:
    def __init__(self, file_path):
        self.file_path = file_path

    def cargar(self):
        return pd.read_csv(self.file_path)