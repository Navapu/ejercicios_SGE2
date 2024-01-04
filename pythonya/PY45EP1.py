class AgendaPersonal:
    def __init__(self):
        self.contactos = []

    def cargar_contacto(self):
        nombre = input("Ingrese el nombre de la persona: ")
        telefono = input("Ingrese el teléfono: ")
        mail = input("Ingrese el correo electrónico: ")
        contacto = {'Nombre': nombre, 'Teléfono': telefono, 'Mail': mail}
        self.contactos.append(contacto)
        print(f"Contacto de {nombre} agregado a la agenda.")

    def listar_agenda(self):
        print("Listado completo de la agenda:")
        for contacto in self.contactos:
            print(f"Nombre: {contacto['Nombre']}, Teléfono: {contacto['Teléfono']}, Mail: {contacto['Mail']}")

    def consultar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto['Nombre'] == nombre:
                print(f"Información del contacto de {nombre}:")
                print(f"Teléfono: {contacto['Teléfono']}, Mail: {contacto['Mail']}")
                return
        print(f"No se encontró el contacto de {nombre} en la agenda.")

    def modificar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto['Nombre'] == nombre:
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                nuevo_mail = input("Ingrese el nuevo correo electrónico: ")
                contacto['Teléfono'] = nuevo_telefono
                contacto['Mail'] = nuevo_mail
                print(f"Contacto de {nombre} modificado.")
                return
        print(f"No se encontró el contacto de {nombre} en la agenda.")

    def menu(self):
        while True:
            print("\nMenú de la Agenda Personal:")
            print("1. Cargar un contacto")
            print("2. Listar la agenda")
            print("3. Consultar un contacto por nombre")
            print("4. Modificar teléfono y mail de un contacto")
            print("5. Finalizar programa")

            opcion = input("Ingrese la opción deseada (1-5): ")

            if opcion == '1':
                self.cargar_contacto()
            elif opcion == '2':
                self.listar_agenda()
            elif opcion == '3':
                nombre = input("Ingrese el nombre de la persona a consultar: ")
                self.consultar_contacto(nombre)
            elif opcion == '4':
                nombre = input("Ingrese el nombre de la persona a modificar: ")
                self.modificar_contacto(nombre)
            elif opcion == '5':
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")

# Crear una instancia de la clase AgendaPersonal
agenda = AgendaPersonal()

# Ejecutar el menú
agenda.menu()
