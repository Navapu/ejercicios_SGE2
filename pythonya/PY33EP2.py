def cargar_productos():
    productos = []
    for _ in range(5):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input(f"Ingrese el precio de {nombre}: "))
        productos.append((nombre, precio))
    return productos

def listar_productos(productos):
    print("Lista de productos y precios:")
    for nombre, precio in productos:
        print(f"{nombre}: ${precio:.2f}")

def imprimir_precios_entre_10_y_15(productos):
    print("Productos con precios entre $10 y $15:")
    for nombre, precio in productos:
        if 10 <= precio <= 15:
            print(f"{nombre}: ${precio:.2f}")

# Paso 1: Cargar productos por teclado
productos_cargados = cargar_productos()

# Paso 2: Listar productos y precios
listar_productos(productos_cargados)

# Paso 3: Imprimir productos con precios entre $10 y $15
imprimir_precios_entre_10_y_15(productos_cargados)
