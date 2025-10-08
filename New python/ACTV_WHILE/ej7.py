import random
maquina = random.randint (1, 10)
usuario = int(input("Adivina el número que escogió la máquina: "))
while usuario != maquina:
    print("No has acertado")
    usuario = int(input("Adivina el número que escogió la máquina..: "))
print("Acertaste!!")