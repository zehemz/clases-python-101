#crear lista de 0-100

lista=[]
lista=range(101)
lista_out=[]
print lista

for x in lista:
    if x<50:
        print x
        lista_out.append(x)

print lista_out
raw_input("enter para salir")    
        
