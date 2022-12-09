def despedir():
    print("Adios")
    print("Hasta Luego")

class Despedida:
    def __init__(self, nombre):
        self.nombre = nombre
    def despedir(self):
        print("Adios", self.nombre)
        print("Hasta Luego", self.nombre)
        