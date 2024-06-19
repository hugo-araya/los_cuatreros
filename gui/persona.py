class Persona():
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def imprimir(self):
        print('Nombre:', self.nombre + " " + self.apellido)

if __name__ == "__main__":
    objeto1 = Persona("Cristian", "Mella")
    objeto1.imprimir()

    objeto2 = Persona("Hugo", "Araya")
    objeto2.imprimir()
