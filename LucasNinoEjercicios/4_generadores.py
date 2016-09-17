
def pares(n):
    index = 1
    while index<(n+2)/2 :
        yield index*2
        index = index + 1


if __name__ == '__main__':
    k=input("ingrese n")
    for i in pares(k):
        print i
    raw_input("enter para salir")
        
