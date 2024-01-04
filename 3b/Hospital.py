class PersonalHospital:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Medico(PersonalHospital):
    def __init__(self, dni, nombre, direccion, telefono, especialidad):
        super().__init__(dni, nombre, direccion, telefono)
        self.especialidad = especialidad

class Enfermero(PersonalHospital):
    def __init__(self, dni, nombre, direccion, telefono, planta):
        super().__init__(dni, nombre, direccion, telefono)
        self.planta = planta

class Paciente:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial = []

    def agregar_prueba(self, fecha, medico_atendio):
        prueba = {'fecha': fecha, 'medico_atendio': medico_atendio}
        self.historial.append(prueba)

# Programa principal
if __name__ == "__main__":
    # Crear personal del hospital
    medico1 = Medico("12345678A", "Dr. Smith", "Calle Hospital", "123456789", "Cardiología")
    enfermero1 = Enfermero("98765432B", "Enfermero López", "Calle Hospital", "987654321", "Planta 3")

    # Crear paciente
    paciente1 = Paciente("78901234C", "Juan Pérez", "Calle Paciente", "567890123")

    # Agregar pruebas al historial del paciente
    paciente1.agregar_prueba("2023-01-01", medico1)
    paciente1.agregar_prueba("2023-02-15", medico1)

    # Mostrar información del paciente
    print(f"Información del paciente {paciente1.nombre}:")
    print(f"DNI: {paciente1.dni}")
    print(f"Dirección: {paciente1.direccion}")
    print(f"Teléfono: {paciente1.telefono}")

    print("\nHistorial de pruebas:")
    for prueba in paciente1.historial:
        print(f"Fecha: {prueba['fecha']}, Médico: {prueba['medico_atendio'].nombre} ({prueba['medico_atendio'].especialidad})")
