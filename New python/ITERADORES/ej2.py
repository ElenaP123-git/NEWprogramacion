altura_maxima = int(input("Dame un número (altura del triángulo): "))

# 'i' será la variable de control (empieza en la primera fila)
i = 1

print("--- Triángulo ---")
while i <= altura_maxima:  # Condición: repetir mientras i no exceda su altura máxima
    
    # CORRECCIÓN: Usamos 'i' para dibujar los asteriscos (fila1, dibuja 1, fila 2, dbuja 2...).
    estrella = "*" * i
    i = i + 1 
    print(estrella)
    
    # CORRECCIÓN: Incrementamos 'i' para que el dibujo crezca y el bucle termine.
    
    
print("--- Fin del Dibujo ---")
