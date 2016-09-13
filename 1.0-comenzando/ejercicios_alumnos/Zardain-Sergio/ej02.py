#Evaluar 4>3 and print("hola") - Explicar que sucede, generar un ejemplo donde la sentencia "hola" NO se ejecute.
i = 4
while i != 0:
	if i > 3:
		print("hola")
		i = 3
	else:
		print("chau")
		i = 0
	

#lo que sucede es que evalua la condición lógica 4 > 3, al ser verdadero ejecuta la sentencia del scope del "if",
#si esa sentencia no se cumple se ejecuta lo que se encuentra en el scope del "else"
