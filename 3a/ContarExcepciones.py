import sys

try:   
    for i in range(int(sys.argv[1]), int(sys.argv[2])):
        print(i)
except:
    print("Datos incorrectos")