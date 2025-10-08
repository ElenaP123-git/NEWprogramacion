suma = 0
N1 = int(input("Ingrese un número: "))
N2 = int(input("Ingrese un número 2: "))
while N1 !=0 or N2 !=0: #estadística :) (independientes)
    suma= suma + N1
    suma = suma + N2
    print("La suma es:", suma) #para que salga la suma de dos en dos y no continúe preguntando
    N1 = int(input("Ingrese un número..: "))
    N2 = int(input("Ingrese un número 2..: "))
print("FIN")
