#crear lista de 0-100

#lista=[]
#lista=range(101)
#lista_out=[]
#print lista

#for x in lista:
#    if x<50:
#        print x
#        lista_out.append(x)
#    else:
#        print x*2
#        lista_out.append(x*2)

#print lista_out


lista= range (101)
print"lista de entrada:\n", lista,"\n\n" 

lista_out= filter((lambda x: x<50),lista)
print "lista filtrada:\n",lista_out
raw_input("enter para salir")
