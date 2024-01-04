# Importar funciones sqrt y pow del módulo math con alias
from math import sqrt as raiz_cuadrada, pow as potencia

# Utilizar las funciones con alias
numero = 25

# Calcular la raíz cuadrada con el alias
resultado_raiz_cuadrada = raiz_cuadrada(numero)
print(f"La raíz cuadrada de {numero} es: {resultado_raiz_cuadrada}")

# Calcular la potencia con el alias
exponente = 3
resultado_potencia = potencia(numero, exponente)
print(f"{numero} elevado a la {exponente} es: {resultado_potencia}")
