def contar_mayores_de_edad(*edades):
    mayores_de_edad = [edad for edad in edades if edad >= 18]
    cantidad_mayores_de_edad = len(mayores_de_edad)
    return cantidad_mayores_de_edad

edades_ingresadas = [15, 22, 17, 30, 18, 25]
cantidad_mayores = contar_mayores_de_edad(*edades_ingresadas)

print(f"La cantidad de personas mayores o iguales a 18 años es: {cantidad_mayores}")
