n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce un segundo número: "))

while n1 == 0 and n2 == 0:
    n1 = int(input("Introduce un número: "))
    n2 = int(input("Introduce un segundo número: "))
if n1<n2:
    for i in range (n1 ,n2 + 1):
        print(i)
else:
    for i in range (n2 ,n1 + 1):
        print(i)