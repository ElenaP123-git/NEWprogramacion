
print("=====================")
print("SOMBRERO SELECCIONADOR")
print("=====================")
print("1. Seleccionar casa para el alumno")
print("2. Mostrar estadísticas")

opcion= int(input("Introducir opción: "))
while opcion != 1 and opcion !=2:
    opcion= int(input("Introducir opción: "))
if opcion == 1:
    print("Ejecutando y seleccionando casa...")
    import random
    nombre = input("Introduce nombre alumno: ")
    maquina = random.randint(1,4)
    if maquina == 1:
        maquina = "Gryffindor"
        print("El sombrero dice que", nombre, "pertenece a", maquina)
    elif maquina == 2:
        maquina = "Slytherin"
        print("El sombrero dice que", nombre, "pertenece a", maquina)
    elif maquina == 3:
        maquina = "Hufflepuff"
        print("El sombrero dice que", nombre, "pertenece a", maquina)
    elif maquina == 4:
        maquina == "Ravenclaw"
        print("El sombrero dice que", nombre, "pertenece a", maquina)
    elif opcion == 2:
        print("mostrando estadísticas")
