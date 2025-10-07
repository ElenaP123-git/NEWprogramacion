total = 0
for i in range(3, 30, 4):
    if i % 5 == 0: # si el número i es múltiplo de 5
	    total = total + i
print(total)