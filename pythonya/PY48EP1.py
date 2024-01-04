class Jugador:
    tiempo=30

    def __init__(self, nombre, puntaje):
        self.nombre=nombre
        self.puntaje=puntaje

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Puntaje:",self.puntaje)
        print("Fin de juego en",Jugador.tiempo,"minutos")

    def pasar_minuto(self):
        Jugador.tiempo=Jugador.tiempo-1



jugador1=Jugador("Juan",100)
jugador2=Jugador("Ana",50)
while Jugador.tiempo>0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_minuto()