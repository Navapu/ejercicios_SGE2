def cargar_lista():
    lista = []
    for _ in range(10):
        elemento = int(input("Ingrese un entero: "))
        lista.append(elemento)
    return lista

def obtener_primer_mitad(lista):
    mitad = len(lista) // 2
    return lista[:mitad]

def imprimir_lista(lista):
    print("Lista:", lista)

# Paso 1: Cargar una lista de 10 enteros
mi_lista = cargar_lista()

# Paso 2: Obtener la primer mitad de la lista
primer_mitad = obtener_primer_mitad(mi_lista)

# Paso 3: Imprimir la lista resultante
imprimir_lista(primer_mitad)
