numero = int(input("Número: "))
resultado = numero
for num in range (numero - 1, 0, -1):
    print(num,"*", resultado)
    resultado = resultado * numero
    print(resultado)
print("Fin")

#OJITO
