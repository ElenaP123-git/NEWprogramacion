print("SOMBRERO SELECCIONADOR")
print("=====================")
print("1. Seleccionar casa para el alumno")
print("2. Mostrar estadísticas")

total_alumnos = 0
Gry = 0
Sly= 0
Huf = 0
Rav = 0
contador = 0

opcion= int(input("Introducir opción: "))
while opcion != 1 and opcion !=2:
    opcion= int(input("Introducir opción: "))
if opcion == 1:
    print("Ejecutando y seleccionando casa...")
    import random
    nombre = input("Introduce nombre alumno: ") . lower()
    if nombre == "voldemort":
        print("Apparition, transpórtame a orto sitio")
        print("Fin")
    else:
        while nombre != "Voldemort":
            maquina = random.randint(1,4)
            if maquina == 1:
                maquina = "Gryffindor"
                contador +=1
                Gry += 1
                print("El sombrero dice que", nombre, "pertenece a", maquina)
            elif maquina == 2:
                maquina = "Slytherin"
                contador +=1
                Sly +=1
                print("El sombrero dice que", nombre, "pertenece a", maquina)
            elif maquina == 3:
                maquina = "Hufflepuff"
                contador +=1
                Huf += 1
                print("El sombrero dice que", nombre, "pertenece a", maquina)
            else:
                print("El sombrero dice que", nombre, "pertenece a", "Ravenclaw")
                contador +=1
                Rav +=1
    
            opcion= int(input("Introducir opción: "))
            nombre = input("Introduce nombre alumno: ") . lower()
            print("=====================")    
            print("SOMBRERO SELECCIONADOR")
            print("=====================")
            print("1. Seleccionar casa para el alumno")
            print("2. Mostrar estadísticas")
elif opcion == 2:
    total_alumnos = Gry + Sly + Huf + Rav
    print("Mostrando estadísticas...")
    print("Total de alumnos: ", total_alumnos)
    print("Gryffindor: ",Gry)
    print("Slytherin: ",Sly)
    print("Hufferpuff: ",Huf)
    print("Ravenclaw: ",Rav)

# :(