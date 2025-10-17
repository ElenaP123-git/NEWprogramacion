nombre = input("Introduce el nombre del alumno: ")
opcion= int(input("Introducir opción: "))
print("=====================")
print("SOMBRERO SELECCIONADOR")
print("=====================")
while opcion != 1 and opcion !=2:
    opcion= int(input("Introducir opción: "))
if opcion == 1:
    print("Ejecutando y seleccionando casa...")
    print("Seleccionar casa para el alumno")
elif opcion == 2:
    print("Mostrar estadísticas")


