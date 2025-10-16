dia = int(input("Introduce el día actual: ")) 
mes = int(input("Introduce el mes que es: "))
hemisferio = input("Ahora introduce el hemisferio: ").lower()

while hemisferio != "norte" and hemisferio != "sur":
    hemisferio = input("Introduce el hemisferio de nuevo: ").lower()
if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("FIN: fecha introducida incorrecta")
else:
    if (mes == 9 and dia >=23) or (mes == 10 or mes ==11) or (mes ==12 and dia <21):
        estacion = "Otoño"
    elif (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia < 21):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia < 21):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia < 23):
        estacion = "Verano"
    else:
        print("ERROR: fecha inválida")
    match hemisferio:
        case "sur":
            if estacion == "Otoño":
                print("Primavera")
            elif estacion == "Invierno":
                print("Verano")
            elif estacion == "Primavera":
                print("Otoño")
            elif estacion == "Verano":
                print("Invierno")
            else:
                print(estacion)
        case "norte":
            print(estacion)
        case _:
            print("ERROR")
            
