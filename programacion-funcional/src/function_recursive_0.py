'''
Created on Jul 25, 2016

@author: zehemz
'''

def sumatoria(lista):
    if len(lista) == 0:
        return 0
    return lista.pop() + sumatoria(lista)

if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8]
    print(sumatoria(lista))