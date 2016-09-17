def sumatoria (val):
    suma_num = 0
    for i in range (val + 1):    
        suma_num += i
    return suma_num

#    print "resultado de la sumatoria >> " + str (suma_num)

def factorial (val):
    res = 1
    fac = 1
    for i in range (val):
        res = res*fac
        fac += 1
    return res

while True:
    
    resultado = 0
    numero = input ("ingrese un numero entero >>> ")
    operacion = raw_input ("para factorial pulse f o para sumatoria pulse s >>> ")

    if (operacion == "f"):
        resultado = factorial(numero)

    elif (operacion =="s"):
        resultado = sumatoria(numero)

    else:
        print ("error, caracter no esperado, ingrese f o s")
        resultado = "ERROR"

    print ("el resultado de la operacion es",resultado)
    
