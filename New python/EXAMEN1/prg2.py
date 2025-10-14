dia = int(input("Introduce el día actual: ")) 
mes = int(input("Introduce el mes que es: "))
hemisferio = input("Ahora introduce el hemisferio: ")
while hemisferio != "norte" or "sur":
    hemisferio = input("Introduce el hemisferio de nuevo: ")
match hemisferio:
    case "norte":
        if 23 <= dia <= 30 and mes == 9:
            print("Otoño")
        elif 21 <= dia <= 31 and mes == 12:
            print("Invierno")
        elif 21 <= dia <= 31 and mes == 3:
            print("Primavera")
        elif 21 <= dia <= 30 and mes == 6:
            print("Verano")
        else:
            print("ERROR")
    case "sur":
        if 23 <= dia <= 30 and mes == 9:
            print("Primavera")
        elif 21 <= dia <= 31 and mes == 12:
            print("Verano")
        elif 21 <= dia <= 31 and mes == 3:
            print("Otoño")
        elif 21 <= dia <= 30 and mes == 6:
            print("Invierno")
        else:
            print("ERROR")
    case _ if dia > 31 or mes > 12:
        print("FIN")
        