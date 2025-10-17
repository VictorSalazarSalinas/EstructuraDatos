import numpy as np


#creacion de una matriz 3X3
matriz_A=np.array([
					[1,2,3,5],
					[4,5,6,4],
					[7,8,9,3],
					[6,7,3,0]
	])
z=0
suma=0
for fila in matriz_A:
	for elemento in fila:
		z=z+1
		suma=suma+elemento
		print(elemento,end="")
	print("")
	
pro=suma/z
print(suma,"  suma  ",pro, "   promedio")

print("deseas modificar una temperatuta")
mod=int(input("1:si  2:no"))

if mod==1:
	fila=int(input("dame fila"))
	columna=int(input("dame la columna"))
	valor=int(input("dame la nueva temperatuta"))
	matriz_A[fila,columna]=valor


for fila in matriz_A:
	for elemento in fila:
		suma=suma+elemento
		print(elemento,end="")
	print("")


pro=suma/z
print(suma,"  suma  ",pro, "   promedio")