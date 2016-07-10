'''
Created on 9 jul. 2016

@author: Lucas
'''

import pickle

if __name__ == '__main__':
    lista = [1,2,3,4,5]
    diccionario = {'nombre': 'lucas', 'apellido' : 'bais'}
    
    pickle.dump(lista, open("lista.p", "wb"))
    pickle.dump(diccionario, open("diccionario.p", "wb"))
    
    nuevaLista = pickle.load(open("lista.p", "rb"))
    nuevoDic = pickle.load(open("diccionario.p", "rb"))
    
    print(nuevaLista)
    print(nuevoDic)
    