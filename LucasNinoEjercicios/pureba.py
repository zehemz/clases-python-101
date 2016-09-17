from Nota_alumnos import *

while True:
           
    accion = raw_input("PARA LEER PRESIONE l  PARA GUARDAR PRESIONE g :\n")
    if accion == "l":
        leer()
    elif accion == "g":
        guardar()
    elif accion == "t":
        print (dic)
    else:
        print ("error de seleccion")
