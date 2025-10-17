import numpy as np


#creacion de una matriz 3X3
matriz_A=np.array([
					[1,2,3],
					[4,5,6],
					[7,8,9]
	])

for fila in matriz_A:
	for elemento in fila:
		print(elemento,end="")
	print("")

print("deseas modificar una calificacion")
mod=int(input("1:si  2:no"))

if mod==1:
	fila=int(input("dame fila"))
	columna=int(input("dame la columna"))
	valor=int(input("dame la nueva calificacion"))
	matriz_A[fila,columna]=valor

promedio=0
n=1
for fila in matriz_A:
	for elemento in fila:
		promedio=promedio+elemento
		n=n+1

		print(elemento,end="")
	print("")

print("promedio genral del grupo",(promedio/n))