# Mostrar los números del 5 al 50 que sean múltiplos de 5.
print("Múltiplos de 5 (del 5 al 50): ")
for numero in range(5, 51,5):
    if numero % 5 == 0: # Comprueba si el resto de la división por 5 es 0
        print(numero)