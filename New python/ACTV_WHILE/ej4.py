suma = 0 #para acumular los números en bucle
N1 = int(input("Ingrese un número: "))
while N1 != 0:
    suma= suma + N1 #para sumar en bucle
    N1 = int(input("Ingrese un número...: ")) #para preguntar número tras número hasta que sea 0
print("Total =",suma)
