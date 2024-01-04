def cargar_lista():
    lista = []
    for i in range(10):
        elemento = int(input(f"Ingrese el elemento {i + 1}: "))
        lista.append(elemento)
    return lista

def separar_positivos_negativos(lista):
    positivos = [num for num in lista if num > 0]
    negativos = [num for num in lista if num < 0]
    return positivos, negativos

def imprimir_listas(positivos, negativos):
    print("Lista de positivos:", positivos)
    print("Lista de negativos:", negativos)

# Paso 1: Cargar una lista de 10 elementos enteros
mi_lista = cargar_lista()

# Paso 2: Generar dos listas a partir de la primera
positivos, negativos = separar_positivos_negativos(mi_lista)

# Paso 3: Imprimir las dos listas generadas
imprimir_listas(positivos, negativos)