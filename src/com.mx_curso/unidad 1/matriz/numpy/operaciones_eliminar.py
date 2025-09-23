import numpy as np

datos =np.array([[10,1,10],
				[10,10,10],
				[10,2,10]])

print(datos)
print()

datos_limpios=np.delete(datos,1,axis=0)

print(datos_limpios)
print()

datos[0]=[1,-2,2]
datos[1]=[1,2,-2]
datos[2]=[1,2,2]


print(datos)

valores_negativos=[]

for i in range(datos.shape[0]):
	for j in range(datos.shape[1]):
		if datos[i,j] < 0:
			valores_negativos.append([i,j])
			
		
datos_limpios=np.delete(datos,valores_negativos,axis=0)

print()
print(datos_limpios)


