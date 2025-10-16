num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un segundo número: "))

while num1 <11 or num2 <11:
    print("Error: escoge números igual o mayores a 11")
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce un segundo número: "))

if num1 < num2:
    for i in range (0, num2 + 1,11):
        if i > num1:
            print(i)
else:
    for i in range (0,num1 + 1,11):
        if i > num2:
            print(i)
