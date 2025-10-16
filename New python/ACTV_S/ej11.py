total = 0 #almacena la suma acumulada
for i in range(1, 16, 2):
	total = total + i
print(total)
#Da 64 por la suma de todos los numeros en bucle hasta el 15 Iteración:

#          Valor de i	  Operación: total + i	  Nuevo total
#Inicial	    —	              —	                0
#1           	1	             0+1            	1
#2          	3	             1+3	            4
#3          	5	             4+5	            9
#4           	7	             9+7	            16
#5	            9	            16+9	            25
#6	            11	            25+11	            36
#7	            13	            36+13           	49
#8	            15	            49+15	            64
