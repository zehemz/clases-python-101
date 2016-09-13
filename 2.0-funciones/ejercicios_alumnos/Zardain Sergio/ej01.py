#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

# Dado una lista de números enteros definir una nueva lista que indica la tupla numero-paridad(true/false)
if __name__ == "__main__":
    tupla = list((x, (x % 2 == 0)) for x in [x for x in range(10)])
    print(tupla)
