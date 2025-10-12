N = int(input("Ingrese la altura del cuadrado (N): "))
# Fila de relleno interior (ej. para N=5, es '*###*')

relleno_interior = "#" * (N - 2) 
fila_relleno = "*" + relleno_interior + "*" 

# Fila de borde completo (ej. para N=5, es '*****')
fila_borde = "*" * N 

print("--- Patrón Dibujado ---")
for i in range(1, N + 1):
    
    # Condición de Borde (Primera o Última fila)
    if i == 1 or i == N:
        print(fila_borde)
    else:
        # Imprime las filas interiores (ej. *###*)
        print(fila_relleno)

print("Fin")