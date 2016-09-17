#a=0
#lista = []
#lista_2 = []
#while True :
   
   #entrada = raw_input()
   #lista.append(entrada)
   #lista_2.append(entrada)
   #print lista
   #print "mi nombre es " + lista_2 [a]
   #a+=1 
#-------------------------------archivo---------------
#archivo = open("nuevo.txt","r")
#contenido = archivo.readline()
#print contenido

#-----------------------------url navegador----------
#import webbrowser
#webbrowser.open_new_tab("http://www.google.com.ar")
#----------------------------------------------------


#print archivo

while True:
    archivo= open ("archivo.py")
    raw_input()
    k= 0
    for i in archivo:
        k += 1 
        print k,")",i
    raw_input("enter para salir")
