class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor entero: "))
        self.valor2 = int(input("Ingrese el segundo valor entero: "))

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: No se puede dividir por cero."

    def imprimir_resultados(self):
        print("Resultados:")
        print("Suma:", self.suma())
        print("Resta:", self.resta())
        print("Multiplicación:", self.multiplicacion())
        print("División:", self.division())

# Crear una instancia de la clase Operaciones
operaciones_instancia = Operaciones()

# Imprimir los resultados
operaciones_instancia.imprimir_resultados()
