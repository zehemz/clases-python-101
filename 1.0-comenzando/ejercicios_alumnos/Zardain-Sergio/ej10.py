# -*- coding: utf-8 -*-
import random
from time import sleep
#SUPER HARD, vale 10 puntos para Griffindor: Escribir un piedra, papel o tijera de 1 ronda.

print "***** Piedra, papel o tijera (el mejor de 3 intentos) *****"
print ""
sleep(1)

#Funcion que realiza la lógica del juego

constanteIntentos=3
intentos = 1

#	1- Piedra
#	2- Papel
#	3- Tijera

#	0- Perdi con la CPU
#	1- Gané a la CPU
#	2- Empatamos

# [PIEDRA,PAPEL,TIJERA]

matrizJuego = [[2,0,1],[1,2,0],[0,1,2]]
matrizTexto = [0,"Piedra","Papel","Tijera"]

while str(intentos) != constanteIntentos:
  print "intento n°: " + str(intentos)
  print " "
# Valido que haya ingresado un número
  ingreseValor=0
  while ingreseValor == 0:
    print "¿Piedra(1), papel(2) o tijera(3)?"
    opcion = raw_input()
    if opcion.isdigit():
      ingreseValor=1
      if int(opcion) > 0 and int(opcion) < 4:
          print "...", matrizTexto[int(opcion)]
          print " "
    else:
      print "	ingrese un numero, reintente."
      print " "
      ingreseValor=0

#PC, opción al azar
  sleep(1)
  azar = random.choice([1,2,3])
  print "PC eligió...", azar,matrizTexto[azar]

#Muestro el resultado
  if matrizJuego[int(opcion)][int(azar)] == 0:
	print "Perdiste."
  elif matrizJuego[int(opcion)][int(azar)] == 1:
	print "Ganaste!"
  else:
	print "Empate..."
  sleep(1)
  print ""
  intentos += 1
print "PARTIDA TERMINADA"
