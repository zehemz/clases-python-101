lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista_2=[]
print lista,"\n"
for x in lista:
    if x%2:
        tupla=(x,False)
        lista_2.append(tupla)
    else:
        tupla=(x,True)
        lista_2.append(tupla)
        
print  lista_2
raw_input("enter para salir")
