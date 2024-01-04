class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre
        self.equipo = None
    
    def anadirequipo(self, equipo):
        self.equipo = equipo
    
    def mostrar(self):
        if(self.equipo != None):
            print(f"{self.dorsal}. {self.nombre} juega en el {self.equipo}")
        else:
            print(f"{self.dorsal}. {self.nombre} no pertenece a ningún equipo")
    


class Equipo:
    def __init__(self, equipo):
        self.equipo = equipo

    def getequipo(self):
        return self.equipo

e = Equipo("Valencia")

j1 = Jugador(15, "Pau Gasol")
j2 = Jugador(25, "Alejandro Navarro")
j1.anadirequipo(e.getequipo())
j1.mostrar()
j2.mostrar()