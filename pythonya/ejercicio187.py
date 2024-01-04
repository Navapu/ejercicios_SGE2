class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_informacion(self):
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Nota del alumno: {self.nota}")

    def esta_regular(self):
        return self.nota >= 4

# Crear dos objetos de la clase Alumno
alumno1 = Alumno("Juan Pérez", 3.5)
alumno2 = Alumno("Ana García", 5.2)

# Imprimir información y verificar si están regulares
print("Información del Alumno 1:")
alumno1.imprimir_informacion()
if alumno1.esta_regular():
    print("El alumno está regular.")
else:
    print("El alumno no está regular.")

print("\nInformación del Alumno 2:")
alumno2.imprimir_informacion()
if alumno2.esta_regular():
    print("El alumno está regular.")
else:
    print("El alumno no está regular.")
