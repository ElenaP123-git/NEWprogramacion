N = int(input("Ingrese la altura del cuadrado (N): "))

print("--- Patrón ---")

borde = "*"
relleno_len = N - 2 

#Relleno Impar (solo #)
relleno_impar = "#" * relleno_len

# Relleno Par (@*@*)
repeticiones = relleno_len // 2
relleno_par = "@*" * repeticiones

# Si la longitud del relleno es IMPAR, necesitamos un '@' extra al final.
if relleno_len % 2 != 0:
    relleno_par += "@"

i = 1 
while i <= N:
    es_fila_impar = (i % 2 != 0)
    
    if i == 1 or i == N:
        # Fila 1 y Fila N (Bordes superior/inferior)
        print(borde * N)
        
    elif es_fila_impar:
        # Filas Impares (Relleno de #)
        print(borde + relleno_impar + borde)
        
    else:
        # Filas Pares (Patrón @*)
        print(borde + relleno_par + borde)
    
    # AVANCE del contador de filas
    i = i + 1

print("Fin")

#HELP