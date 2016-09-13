import random

diccionarioAlumnos = {}
diccionarioMaterias = {}

if __name__ == "__main__":
	# materias de la carrera
	while(True):
		# Ingresa Nombre Carreta SErGIO
		nombreMateria = input("Ingrese nombre de la Carrera: ")

		continuo = True
		while (continuo):
			idMateria = int(str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)))

			if idMateria in diccionarioMaterias.keys():
				continuo = True
			else:
				continuo = False

		# Ingreso los alumnos en una lista
		while(True):
		    # valido los caracteres del nombre
		    while(True):
		        nombreAlumno = input("Ingrese nombre del alumno: ")
		        if len(nombreAlumno) < 5:
		            print("El nombre debera contener 5 caracteres como minimo.")
		        else:
		            break
		    # valido la longitud de la nota
		    while(True):
		        notaAlumno = float(input("Ingrese la nota del alumno: "))
		        if (notaAlumno >= 0 and notaAlumno <= 10) == False:
		            print("La nota debe estar entre 0 y 10.")
		        else:
		            break
		    # asigno el alumno al diccionario
		    diccionarioAlumnos[nombreAlumno] = notaAlumno

		    # pregunto si desea continuar
		    print(" ")
		    rta = input("Desea cargar mas alumnos? (y/n)")
		    print(" ")
		    if rta != "y":
		        print(" ")
		        break
		diccionarioMaterias[idMateria] = {"nombreMateria":nombreMateria,"alumnos":diccionarioAlumnos}
		print(" ")
		rta = input("Desea cargar mas materias? (y/n)")
		print(" ")
		if rta != "y":
		    print(" ")
		    break
print(" ")
# muestro los nombres y las notas,
for codMateria,diccionarios in diccionarioMaterias.items():
	print("Cod Materia: " + str(codMateria))
	print("Materia: " + diccionarios["nombreMateria"])
	for nombre, nota in diccionarios["alumnos"].items():
		print("Nombre: " + nombre)
		print("Nota: " + str(nota))
