
#permite guardar y leer, nombre y notas de alumnos.


def guardar ():
    nota =0
    nombre =""    
    nombre = raw_input("ingrese su nombre :\n")
    nota= input("ingrese nota, de 0 a 10 :\n")
    if nota<=10 and nota>=0:
        dic[nombre] = (nota)
        print("guardado!")
    else:
        print ("la nota ingresada no es valida (0 -10)") 
        
        
def leer ():
    nombre_leer=""
    nombre_leer = raw_input("nombre a leer >>>\n") 
    print("El alumno: "+(nombre_leer)+"\nTiene la nota: "+ str( dic[nombre_leer]))

dic={}
accion=""        

if __name__ == "__main__":
    
        
    
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
    
