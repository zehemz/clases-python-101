#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from auto import Auto
from auto_volador import AutoVolador
if __name__ == '__main__':
    # Instanciamos e imprimimos el objeto de la clase Auto
    objeto = Auto()
    print(objeto.color)

    print(objeto.encendido)
    # Imprimimos los métodos de la clase Auto
    print(dir(Auto))
    # Vemos cual es su clase padre
    print(Auto.__class__.__base__)
    # Vemos si es un objeto de alguna clase
    print(Auto.__class__)

    autoVolador = AutoVolador()

    print(dir(autoVolador))
    # Vemos cual es su clase padre
    print(autoVolador.__class__.__base__)
    # Vemos si es un objeto de alguna clase
    print(autoVolador.__class__)

    autoVolador.abrocharCinto(True)
    autoVolador.encender()
    autoVolador.despegar()
    autoVolador.acelerar()
    autoVolador.acelerar()
    autoVolador.acelerar()
    autoVolador.aterrizar()
