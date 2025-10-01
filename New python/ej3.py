num2 = int(input("Introduce la cantidad de numeros que quieres sumar: "))
suma = 0
if num2 > 0:
    for i in range(1,num2 + 1):
        suma = suma + i
        print("Acumulado",suma, "sumando", i)
    print("El total de la suma es: ", suma)
else:
    print("FIn")