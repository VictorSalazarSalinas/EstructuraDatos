import numpy as np


#creacion de una matriz 3X3
matriz_A=np.array([
					[1,2,3],
					[4,5,6],
					[7,8,9]
	])


print(matriz_A)


#acceder a un elemento
elemento=matriz_A[1,2]


print(elemento)


#modificar elemento
matriz_A[0,0]=99

for fila in matriz_A:
	for elemento in fila:
		print(elemento,end="")
	print("")












