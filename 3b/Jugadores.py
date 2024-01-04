class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre

    def mostrar(self):
        print(f"{self.dorsal}. {self.nombre}")

j1 = Jugador(16, "Pau Gasol")
j2 = Jugador(25, "Alejandro Navarro")

j1.mostrar()
j2.mostrar()