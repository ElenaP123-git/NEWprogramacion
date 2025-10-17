num = int(input("Introduce el numero de piedras que quieres mostrar (0,5): "))
while num < 0 or num > 5:
    print("ERROR")
    num = int(input("Introduce el numero de piedras que quieres mostrar (0,5): "))

import random
maquina = random.randint (0,5)
apuesta = input("Apuesta par (P) o impar (I)??: ") . upper()

while num != maquina:
    suma = num + maquina
    if apuesta == "P" and suma % 2 == 0:
        print("La suma total es", suma)
        print("Gana humano")
    elif apuesta == "I" and suma % 2 !=0:
        print("La suma total es", suma)
        print("Gana humano")

    elif apuesta == "P" and suma % 2 !=0:
        print("La suma total es", suma)
        print("Gana máquina")
    elif apuesta == "I" and suma % 2 ==0:
        print("La suma total es", suma)
        print("Gana máquina")
    num = int(input("Introduce el numero de piedras que quieres mostrar (0,5): "))
    apuesta = input("Apuesta par (P) o impar (I)??: ")
print("FIN")