'''
Created on 28 ago. 2016

@author: python
'''


#permite guardar y leer, nombre y notas de alumnos. 

if __name__ == "__main__":
    
    def guardar ():
           
        nombre = raw_input("ingrese su nombre :\n")
        email= raw_input("ingrese correo electronico :\n")
        tel = input("ingrese su numero de telefono :\n")
        direccion = raw_input("ingrese direccion :\n")
        
        dic[nombre] = {"correo": email , "telefono":tel , "direccion" : direccion}  
        print "contacto guardado !!\n"
        
        
        
        
    def leer ():
        #nombre_leer=""
        nombre_leer = raw_input("nombre a leer >>>\n") 
        # print((nombre_leer)+" :\n "+ str( dic[nombre_leer]))
        print ("nombre :"+ nombre_leer)
        print ("correo :"+ str(dic[nombre_leer]["correo"]))
        print ("telefono :"+ str(dic[nombre_leer]["telefono"]))
        print ("direccion :"+ str(dic[nombre_leer]["direccion"])+"\n\n")
        
        
        
    def borrar ():
#        nombre_leer=""
        nombre_leer = raw_input("ingrese el concto a borrar >>>\n") 
    #   print((nombre_leer)+" :\n "+ str( dic[nombre_leer]))
        print ("nombre :"+ nombre_leer)
        print ("correo :"+ str(dic[nombre_leer]["correo"]))
        print ("telefono :"+ str(dic[nombre_leer]["telefono"]))
        print ("direccion :"+ str(dic[nombre_leer]["direccion"])+"\n")    
        borr = raw_input("seguro desea eliminar a "+ nombre_leer + "? y/n >>>\n")
        if borr=="y":
            del dic [nombre_leer]
            print "contacto borrado!!\n"
        else:
            return
        
    email=""
    nombre =""
    tel=None
    direccion=""    
        
    dic={nombre:{"correo": email ,"telefono" : tel , "direccion" : direccion }}
    accion=""
    while True:
           
        accion = raw_input("MOSTRAR  >>> m\nGUARDAR  >>> g\nBORARA   >>> b\n ")
        if accion == "m":
            leer()
        elif accion == "g":
            guardar()
        elif accion == "b":
            borrar()
        elif accion == "t":
            print (dic)
        else:
            print ("error de seleccion")
    
