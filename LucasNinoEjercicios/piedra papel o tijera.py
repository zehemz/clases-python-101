
import random

while True:
    
    print "escoja piedra(1) papel(2) o tjeras(3)  \n"
    seleccion = input()
    azar = random.choice ([1,2,3])
    print azar

    if seleccion == azar:
        print "empate, juegue nuevamente"
    elif seleccion == 1 and azar == 2:
        print "usted pierde"

    elif seleccion == 1 and azar == 3:
        print "usted gana!!!"

    elif seleccion == 2 and azar == 1:
        print "usted gana!!!"

    elif seleccion == 2 and azar == 3:
        print "usted pierde"

    elif seleccion == 3 and azar == 1:
        print "usted pierde"

    elif seleccion == 3 and azar == 2:
        print "usted gana!!!"
    
