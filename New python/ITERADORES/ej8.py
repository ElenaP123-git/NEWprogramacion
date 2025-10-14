# Que el programa sume todos los dígitos de uno introducido
num = int(input("Ingrese un número: "))
suma = 0
while num > 0:
    # AISLAR EL DÍGITO
    digito = num % 10  # Ejemplo: 123 % 10 = 3
    
    # ACUMULAR LA SUMA
    suma = suma + digito  # Ejemplo: suma = 0 + 3 = 3
    
    # AVANZAR: Usamos la división entera para eliminar el último dígito y continuar.
    num = num // 10  # Ejemplo: 123 // 10 = 12
    
# El bucle se detiene cuando numero_a_procesar llega a 0.
print("La suma de los dígitos es:", suma)

#OJITO
