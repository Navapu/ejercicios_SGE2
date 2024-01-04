class Cliente:
    clientes_suspendidos = []

    def __init__(self, codigo_cliente, nombre):
        self.codigo_cliente = codigo_cliente
        self.nombre = nombre
        self.cuenta_suspendida = False

    def suspender_cuenta(self):
        self.cuenta_suspendida = True
        if self not in Cliente.clientes_suspendidos:
            Cliente.clientes_suspendidos.append(self)

    def activar_cuenta(self):
        self.cuenta_suspendida = False
        if self in Cliente.clientes_suspendidos:
            Cliente.clientes_suspendidos.remove(self)

    def imprimir_datos_cliente(self):
        print(f"Código de Cliente: {self.codigo_cliente}")
        print(f"Nombre: {self.nombre}")
        estado_cuenta = "Suspendida" if self.cuenta_suspendida else "Activa"
        print(f"Estado de la Cuenta Corriente: {estado_cuenta}")
        print("-" * 30)

# Crear instancias de la clase Cliente
cliente1 = Cliente(1, "Juan Pérez")
cliente2 = Cliente(2, "Ana García")

# Imprimir datos de clientes antes de suspender cuentas
print("Datos de clientes antes de suspender cuentas:")
cliente1.imprimir_datos_cliente()
cliente2.imprimir_datos_cliente()

# Suspender cuentas
cliente1.suspender_cuenta()
cliente2.suspender_cuenta()

# Imprimir datos de clientes después de suspender cuentas
print("\nDatos de clientes después de suspender cuentas:")
cliente1.imprimir_datos_cliente()
cliente2.imprimir_datos_cliente()

# Imprimir datos de clientes con cuentas suspendidas
print("\nClientes con cuentas suspendidas:")
for cliente in Cliente.clientes_suspendidos:
    cliente.imprimir_datos_cliente()
