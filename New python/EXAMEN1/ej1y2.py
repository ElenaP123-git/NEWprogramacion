n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))

while (n1 != 0) and (n2 !=0) and (n3 != 0):
    if (n1 < n2) and (n2 < n3):
        print("creciente")
    elif (n1 > n2) and (n2 > n3):
        print("decreciente")
    else:
        print("desordenado")
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    n3 = int(input("Introduce el tercer número: "))
        
print("FIN (0,0,0)")
