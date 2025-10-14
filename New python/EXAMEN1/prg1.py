nombre_alumno= input("Introduce tu nombre: ").upper #mayúsculas

while nombre_alumno != "EXIT":
    nota= float(input("Introduce tu nota(0-100): "))
    while nota < 0 or nota > 100:
        nota = float(input("Introduce otra vez tu nota: "))
    match nota:
        case _ if 90.0 <= nota <= 100.0:
            print("Sobresaliente")
        case _ if 70.0 <= nota <= 89.9:
            print("Notable")
        case _ if 60 <= nota <= 69.9:
            print("Bien")
        case _ if 50 <= nota <= 59.9:
            print("Suficiente")
        case _ if 0 <= nota <= 49.9:
            print("Suspenso")

    nombre_alumno = input("Introduzca EXIT si terminaste: ").upper
   
