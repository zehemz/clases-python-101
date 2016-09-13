#Escribir un programa que reciba un número entero positivo, devolver la sumatoria de dicho número.
i = int(input("Ingrese un número:"))
acumulador = ""
suma = 0
for j in range(i+1):
    if j > 1: 
        acumulador += " + " + str(j) 
    elif j == 1: 
        acumulador += str(j) 
    suma += j
    
print("la sumatoria es: " + str(suma) + " (" + acumulador + ")")
