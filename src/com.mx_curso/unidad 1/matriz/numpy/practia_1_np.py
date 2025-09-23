import numpy as np

np.random.seed(42)

datos=np.random.rand(5,5)*100


datos[2,3]=-999
datos[4,1]=-150

print(datos)

indices_error=[]

for i in range(datos.shape[0]):
	for j in range(datos.shape[1]):
		if datos[i,j] < 0:
			indices_error.append([i-1])

print(indices_error)
datos_limpios=np.delete(datos,indices_error,axis=1)
print()
print(datos_limpios)


