def mcd(num, num1):
    temp = 0
    while num1 != 0:
        temp = num1
        num1 = num % num1
        num = temp
    return num

def esPrimo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(mcd(20, 12))

for i in range(1, 51):
    print("El numero:", i, esPrimo(i))