#numeros pares que hay del 0 al 10
#for i in range(11,0,-1) y for in range (0,10,2)
num = int(input("Introduce un número: "))
if num>0:
    for i in range (1,num+1,1): #es lo mismo (1,num +1)
        print(i)
else:
    num2 = int(input("El número tiene que ser positivo: "))
    if num2 > 0:
        for i in range(1,num2+1,1):
            print(i)
    else:
        print("El segundo número tampoco es positivo, fin del programa")
print("Fin")