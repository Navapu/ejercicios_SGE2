class Cuenta:
    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}, Monto: ${self.monto:.2f}")


class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)
        self.genera_intereses = False


class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, tasa_interes):
        super().__init__(titular, monto)
        self.plazo = plazo
        self.tasa_interes = tasa_interes

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Plazo de imposición: {self.plazo} días, Tasa de interés: {self.tasa_interes}%")

# Bloque principal
caja_ahorro = CajaAhorro("Juan Pérez", 5000)
plazo_fijo = PlazoFijo("Ana García", 10000, 30, 5)

print("Información de la Caja de Ahorro:")
caja_ahorro.mostrar_informacion()

print("\nInformación del Plazo Fijo:")
plazo_fijo.mostrar_informacion()
