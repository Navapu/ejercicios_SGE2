def calcular_factorial(n):
    if n < 0 or n > 10:
        return "Error: El número debe estar en el rango de 0 a 10."
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

numero = int(input("Ingrese un número entre 0 y 10: "))

resultado = calcular_factorial(numero)

if type(resultado) == int:
    print(f"El factorial de {numero} es: {resultado}")
else:
    print(resultado)
