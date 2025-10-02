estudiantes=int(input("Número de estudiantes: ")) 
examenes=3 
calificaciones=[] 
# Ingreso de datos 
for i in range(estudiantes): 
	print(f"Estudiante {i+1}") 
	fila=[] 
	for j in range(examenes): 
		nota=float(input(f"Nota del examen {j+1}: ")) 
		fila.append(nota) 
	calificaciones.append(fila) 
# Promedio de cada estudiante 
promedios_est=[] 
for fila in calificaciones: 
	promedio=sum(fila)/examenes 
	promedios_est.append(promedio) 
# Promedio de cada examen 
promedios_exam = [] 
for j in range(examenes):  # Recorrer cada columna (examen) 
	suma=0 
	for i in range(estudiantes):  # Recorrer cada fila (estudiante) 
		suma+=calificaciones[i][j]  # Sumar la nota del examen j del estudiante i 
	promedio=suma/estudiantes 
	promedios_exam.append(promedio) 
# Estudiante con nota más alta 
nota_max=-1 
mejor_est=-1 
for i in range(estudiantes): 
	for nota in calificaciones[i]: 
		if nota>nota_max: 
			nota_max=nota 
			mejor_est=i 
# Resultados 
print("\nPromedios por estudiante:") 
for i, prom in enumerate(promedios_est): 
print(f"Estudiante {i+1}: {prom}") 
print("\nPromedios por examen:") 
for j, prom in enumerate(promedios_exam): 
print(f"Examen {j+1}: {prom}") 
print(f"\nEstudiante con la mejor calificación: Estudiante {mejor_est+1} (nota: 
{nota_max})")