import numpy as np

matriz_A=[[1,2,3],
		  [4,5,6],
		  [9,9,9]]

matriz_B=[[1,4,3],
		  [1,6,7],
		  [9,4,99]]


suma=np.add(matriz_A,matriz_B)
print(suma)
print()

multiplicacion=np.dot(matriz_A,	matriz_B)
print(multiplicacion)
print()
vector_e=np.array([1,2,3])
resultado=np.dot(matriz_A,vector_e)
print(resultado)