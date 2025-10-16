sangre1 = input("Introduce tipo de sangre: ").upper()
sangre2 = input("Introduce el siguiente grupo sanguíneo: ").upper()

if sangre1 == "0-":
    if sangre2 == "0+" or sangre2 == "A-" or sangre2 == "A+" or sangre2 == "B-" or sangre2 == "B+" or sangre2 == "AB-" or sangre2 == "AB+":
        print("COMPATIBLE...")
        print(sangre1,"Puede donar a", sangre2)
    elif sangre2 == "0-":
        print("COMPATIBILIDAD")
        print(sangre1, "puede recibir", sangre2)
    else:
        print("Incompatible")

elif sangre1 == "0+":
    if sangre2 == ("A+" or "B+" or "AB+"): #forma más sencilla
        print("COMPATIBLE...")
        print(sangre1, "puede donar a", sangre2)
    elif sangre2 == "0+" or sangre2 == "0-":
        print(sangre1, "puede recibir de", sangre2)
    else:
        print("Incompatible")

elif sangre1 == "A-":
    if sangre2 == "A+" or sangre2 == "AB+" or sangre2 == "AB-":
        print("COMPATIBLE...")
        print(sangre1, "puede donar a", sangre2)
    elif sangre2 == "A-" or sangre2 == "O-":
        print(sangre1, "puede recibir de", sangre2)
    else:
        print("Incompatible")

elif sangre1 == "A+":
    if sangre2 == "AB+":
        print("COMPATIBLE...")
        print(sangre1, "puede donar a", sangre2)
    elif sangre2 == "A+" or sangre2 == "A-" or sangre2 == "0+" or sangre2 == "0-":
        print(sangre1, "puede recibir de", sangre2)
    else:
        print("Incompatible")

elif sangre1 == "B-":
    if sangre2 == "AB+" or sangre2 == "AB-" or sangre2 == "B+":
        print("COMPATIBLE...")
        print(sangre1, "puede donar a", sangre2)
    elif sangre2 == "B-" or sangre2 == "O-":
        print(sangre1, "puede recibir de", sangre2)
    else:
        print("Incompatible")

elif sangre1 == "B+":
    if sangre2 == "AB+":
        print("COMPATIBLE...")
        print(sangre1, "puede donar a", sangre2)
    elif sangre2 == "B+" or sangre2 == "B-" or sangre2 == "0+" or sangre2 == "0-":
        print(sangre1, "puede recibir de", sangre2)
    else:
        print("Incompatible")

elif sangre1 == "AB-":
    if sangre2 == "AB+":
        print("COMPATIBLE...")
        print(sangre1, "puede donar a", sangre2)
    elif sangre2 == "AB-" or sangre2 == "A-" or sangre2 == "B-" or sangre2 == "0-":
        print(sangre1, "puede recibir de", sangre2)
    else:
        print("Incompatible")

elif sangre1 == "AB+":
    if sangre2 == "AB+":
        print("COMPATIBLE...")
        print(sangre1, "puede donar a", sangre2)
    elif sangre2 == "A+" or sangre2 == "A-" or sangre2 == "0+" or sangre2 == "0-" or sangre2 == "AB-" or sangre2 == "AB+" or sangre2 == "B-" or sangre2 == "B+":
        print(sangre1, "puede recibir de", sangre2)
    else:
        print("Incompatible")
else:
    print("HELP")