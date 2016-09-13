#Modificar el ejercicio anterior generando que únicamente sume números que sean múltiplos de 3, 5 o 7 hasta el número ingresado.
i = int(input("Ingrese un número:"))
acumulador = ""
suma = 0
acumuladorDeTres = 3
for j in range(i+1):
    
    if j % acumuladorDeTres == 0 and j > 0:
        suma += j
        acumuladorDeTres += 2
        if j > 3: 
            acumulador += " + " + str(j) 
        else: 
            acumulador += str(j) 
    
    
print("la sumatoria es: " + str(suma) + " (" + acumulador + ")")
