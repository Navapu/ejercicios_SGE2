def lot(lista):
    lista2 = []
    for i in range(len(lista)):
        if(int(lista[i]) > 49 or int(lista[i]) < 1):
            return "Hay números menores que 1 o mayores que 49"
        else:
            if lista[i] in lista2:
                return "Hay numeros repetidos"
            else:
                lista2.append(lista[i])
    return "Todo esta correcto"
        

        

nums = input("Introduzca los 6 números de la loteria separados por espacios: ")

lista = nums.split(" ")
lista.sort()

print(lista)
print(lot(lista))