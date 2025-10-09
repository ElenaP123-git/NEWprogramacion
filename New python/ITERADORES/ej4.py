# Que un programa pinte el borde del cuadrado
altura_cuadrado= int(input("Introduce la altura del cuadrado: "))
for numfilas in range (altura_cuadrado):
    if numfilas == 0 or numfilas == altura_cuadrado -1:
        print("*" * altura_cuadrado)
    else:
        print("*"+ " " *(altura_cuadrado - 2) + "*")
print("Fin")