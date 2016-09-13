#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

#Dado un número N entero entregar un generador que recorra todos los números pares <= a N.
if __name__ == "__main__":
    numeroN = int(raw_input("ingresar número: "))
    generador = (x for x in range(numeroN) if x % 2 == 0)
    for i in generador:
        print(i)   
