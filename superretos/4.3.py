def es_palindromo(texto):
    # Eliminar espacios y convertir todo a minúsculas
    texto = texto.replace(" ", "").lower()
    
    # Verificar si el texto es un palíndromo
    return texto == texto[::-1]

# Ejemplo de uso
texto_ingresado = input("Ingrese un texto (sin espacios): ")

if es_palindromo(texto_ingresado):
    print(f"{texto_ingresado} es un palíndromo.")
else:
    print(f"{texto_ingresado} no es un palíndromo.")
