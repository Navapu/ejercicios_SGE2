def val(cadena):
    num=0
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u":
            num=num+1
    print("numidad de vocales de la palabra",cadena,"es: ",num)


val("telefono")
val("murcielago")
val("ordenador")