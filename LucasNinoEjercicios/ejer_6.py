

def multiplo(val):
#Utilizmos la funcion modulo para calcular el resto
    rest_3 = val % 3
    rest_5 = val % 5
    rest_7 = val % 7
    if rest_3 == 0 or rest_5 == 0 or rest_7 ==0:
        return True
    else:
        return False

while True:
    suma_num = 0
    valor = input ("ingrese un numero entero positivo multiplo de 3, 5 o 7 >> ")
    num = multiplo(valor)
    if num :
        for i in range (valor + 1):    
            suma_num += i
        print "resultado de la sumatoria >> " + str (suma_num)
    else:
        print "el numero no es multiplo de 3, 5 o 7"

    
