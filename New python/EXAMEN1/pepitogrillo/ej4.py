num = int(input("Introduce un número: "))

suma = 0
while num > 0 and num < 10000:
    num = int(input("Introduce otro número: "))
    suma = suma + 1

    a = num
    if num > a:
        a = num
        num = int(input("Introduce un número: "))

print("Fuera")
print("contador", suma) #contador (0,1,2,3,4)
print("máximo: ", a)