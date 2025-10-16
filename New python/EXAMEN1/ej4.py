dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

diastotal = dia
es_bisisesto = año % 4 == 0

for meses in range (1,mes):
    match meses:
        case 1|3|5|7|8|10|12:
            diastotal += 31
        case 2:
            if es_bisisesto:
                diastotal += 29
            else:
                diastotal += 28
        case 4|6|9|11:
            diastotal += 30
print("Han pasado", diastotal, "dias desde el 1 de enero")

