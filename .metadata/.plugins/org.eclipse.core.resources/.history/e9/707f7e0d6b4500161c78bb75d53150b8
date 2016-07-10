'''
Created on 8 jul. 2016
"""Ejemplo de with"""
@author: Lucas
'''

class WithObject(object):
    """context manager class"""
    def __init__(self):
        pass
    
    def __enter__(self):
        print("holiiis")
    def __exit__(self, type, value, traceback):
        print("chauuu")

def ejemplo():
    lista = [1,2,3,4,5]
    for elemento in lista:
        with WithObject():
            print(elemento)
            
    print(lista)
    

if __name__ == '__main__':
    ejemplo()

    



