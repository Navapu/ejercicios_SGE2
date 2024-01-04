def numeroPatrones(texto):
    # Convertir el texto a minúsculas para evitar distinción entre mayúsculas y minúsculas
    texto = texto.lower()

    # Definir los patrones
    patrones = ["00", "101", "abc", "ho"]

    # Inicializar el contador de patrones
    contador = 0

    # Contar el número de ocurrencias de cada patrón en el texto
    for patron in patrones:
        inicio = 0
        while inicio != -1:
            inicio = texto.find(patron, inicio)
            if inicio != -1:
                contador += 1
                inicio += 1

    return contador

# Ejemplo de uso
cadena_ejemplo = "000101ABCabcHOHo"
resultado = numeroPatrones(cadena_ejemplo)

print(f"El número total de patrones encontrados es: {resultado}")
