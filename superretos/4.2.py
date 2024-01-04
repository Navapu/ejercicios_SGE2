def calcular_fibonacci(n):
    if n < 0 or n > 20:
        return "Error: El número debe estar en el rango de 0 a 20."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibo_actual, fibo_anterior = 1, 0
        for _ in range(2, n + 1):
            fibo_actual, fibo_anterior = fibo_actual + fibo_anterior, fibo_actual
        return fibo_actual

numero = int(input("Ingrese un número entre 0 y 20: "))

resultado = calcular_fibonacci(numero)

if type(resultado) == int:
    print(f"El número de Fibonacci para {numero} es: {resultado}")
else:
    print(resultado)
