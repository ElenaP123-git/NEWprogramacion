x = int(input("Introduce un número: "))
contador = 0
while x > 0 and contador <7:
    if x % 2 != 0:
        for i in range (1,5,3):
            print(i)
            x = x - 1
    else:
        x = x - contador
    contador = contador + 1
    print("x: ",x, "contador: ", contador)
print("Resultado: ", x)
print("Fin")
