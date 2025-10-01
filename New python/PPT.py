#Piedra, papel o tijeras
import random
human = int(input("Introduce 1=PIEDRA, 2=PAPEL O 3=TIJERAS: "))
maquina = random.randint(1,3)
print("Resultado maquina:", maquina)
match human:
    case 1:
        if maquina ==2:
            print("Máquina gana")
        elif maquina == 3:
            print("Humano gana")
        else:
            print("Empate")
    case 2:
        if  maquina ==1:
            print("Gana máquina")
        elif maquina == 3:
            print("Gana máquina")
        else:
            print("Empate")
    case 3:
        if maquina ==1:
            print("Gana máquina")
        elif maquina ==2:
            print("Gana humano")
        else:
            print("Empate")
    case _:
        print("Inválido")
print("Fin partida")


            
