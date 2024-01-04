class AdministradorAlumnos:
    def __init__(self):
        self.nombres = [None] * 5
        self.notas = [None] * 5

    def cargar_alumnos(self):
        for i in range(5):
            nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
            nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
            self.nombres[i] = nombre
            self.notas[i] = nota
        print("Alumnos cargados correctamente.")

    def listar_alumnos(self):
        print("Listado de alumnos y notas:")
        for i in range(5):
            print(f"Nombre: {self.nombres[i]}, Nota: {self.notas[i]}")

    def mostrar_notas_mayores_o_iguales_a_7(self):
        print("Alumnos con notas mayores o iguales a 7:")
        for i in range(5):
            if self.notas[i] >= 7:
                print(f"Nombre: {self.nombres[i]}, Nota: {self.notas[i]}")

    def menu(self):
        while True:
            print("\nMenú de opciones:")
            print("1. Cargar alumnos")
            print("2. Listar alumnos")
            print("3. Mostrar alumnos con notas mayores o iguales a 7")
            print("4. Finalizar programa")

            opcion = input("Ingrese la opción deseada (1-4): ")

            if opcion == '1':
                self.cargar_alumnos()
            elif opcion == '2':
                self.listar_alumnos()
            elif opcion == '3':
                self.mostrar_notas_mayores_o_iguales_a_7()
            elif opcion == '4':
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")

# Crear una instancia de la clase AdministradorAlumnos
admin_alumnos = AdministradorAlumnos()

# Ejecutar el menú
admin_alumnos.menu()
