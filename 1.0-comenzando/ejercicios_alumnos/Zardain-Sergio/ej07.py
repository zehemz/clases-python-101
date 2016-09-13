#Dado un numero ingresado por el usuario, dar la posibilidad al mismo de: generar su sumatoria o su factorial.
n = int(input("Ingrese un número:"))
x = 0
y = 0
fac = 0
# Cálculo de Factorial
	for x in n:
		fac=1
		for y in range(1,x+1):
			fac=fac*y
print("Factorial: " + fac)
# Cálculo de Sumatoria
acumulador = ""
suma = 0
j = 0
for j in range(n+1):
    if j > 1: 
        acumulador += " + " + str(j) 
    elif j == 1: 
        acumulador += str(j) 
    suma += j
    
print("Sumatoria: " + str(suma))
