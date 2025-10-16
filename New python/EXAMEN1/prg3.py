#cuantos dias han transcurrido desde el 1 de enero de ese año
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

while mes>12 or dia>31:
    print("ERROR")
    dia = int(input("Introduce el día: "))
    mes = int(input("Introduce el mes: "))
    año = int(input("Introduce el año: ")) #por si introduce mal los datos

suma= 0
match mes:
    case 1:
        if 1 <= dia <= 31: #enero
           suma = 
           print()
    case 2:
        if 1 <= dia <=28:  #febrero
            print()
    case 3:
        if 1 <= dia <= 31:  #marzo
            ...
    case 4:
        if 1 < dia <= 30:  #abril
            ...
    case 5:
        if 1 <= dia <= 31:  #mayo
            ...
    case 6:
        if 1 <= dia <= 30:  #junio
            ...
    case 7:
        if 1 <= dia <= 31:  #julio
            ...
    case 8:
        if 1 <= dia <= 31:  #agosto
            ...
    case 9:
        if 1 <= dia <= 30:  #septiembre
            ...
    case 10:
        if 1 <= dia <= 31:  #octubre
            ...
    case 11:
        if 1 <= dia <= 30:  #noviembre
            ...
    case 12:
        if 1 <= dia <= 31:  #diciembre
            ...
    case _:
        print("ERROR")

#HELP