num = int(input("Introduce el numero de piedras que quieres mostrar (0,5): "))
while num < 0 or num > 5:
    print("ERROR")
    num = int(input("Introduce el numero de piedras que quieres mostrar (0,5): "))
 
humano_gana= 0
maquina_gana = 0
num_total_partidas = 0
apuesta_humana_PAR= 0
apuesta_humana_IMPAR=0

import random
maquina = random.randint (0,5)
apuesta = input("Apuesta par (P) o impar (I)??: ") . upper()

while num != maquina:
    suma = num + maquina
    if apuesta == "P" and suma % 2 == 0:
        print("La suma total es", suma)
        print("Gana humano")
        humano_gana += 1
        num_total_partidas += 1
    elif apuesta == "I" and suma % 2 !=0:
        print("La suma total es", suma)
        print("Gana humano")
        humano_gana += 1
        num_total_partidas += 1

    elif apuesta == "P" and suma % 2 !=0:
        print("La suma total es", suma)
        print("Gana máquina")
        maquina_gana += 1
        num_total_partidas += 1
    elif apuesta == "I" and suma % 2 ==0:
        print("La suma total es", suma)
        print("Gana máquina")
        maquina_gana += 1
        num_total_partidas += 1

    num = int(input("Introduce el numero de piedras que quieres mostrar (0,5): "))
    apuesta = input("Apuesta par (P) o impar (I)??: ")
    if apuesta == "P":
        apuesta_humana_PAR += 1
    else:
        apuesta_humana_IMPAR +=1

print("FIN")
print("Rondas que ganó el jugador: ", humano_gana)
print("Rondas que ganó la máquina", maquina_gana)
print("Número total de partidas: ", num_total_partidas)
if apuesta_humana_PAR > apuesta_humana_IMPAR:
    print("La apuesta humana más frecuente es PAR")
elif apuesta_humana_PAR < apuesta_humana_IMPAR:
    print("La apuesta humana es IMPAR")
else:
    print("La apuesta humana es igual de frecuente como par e impar")