import numpy as np


datos=np.array([[10.9,9.1,29.1,30.1],
				[10.9,9.1,29.1,30.1],
				[10.9,9.1,29.1,30.1],
				[10.9,9.1,29.1,30.1],
				[10.9,9.1,29.1,30.1],
				[10.9,9.1,29.1,30.1],
				[10.9,9.1,29.1,30.1],
				[10.9,9.1,29.1,30.1],
				[10.9,9.1,29.1,30.1],
				[10.9,9.1,29.1,30.1],
				[10.9,9.1,29.1,30.1]])


print("datos originales")
print(datos)

datos[5]=[99.99,99.99,99.99,99.99]

datos[1,1]=np.nan
datos[5,2]=np.nan
datos[9,3]=np.nan


print("datos con errores",datos)


datos_sinErrores=np.delete(datos,5,axis=0)

print("datos sin errores ",datos_sinErrores)


media_columna=np.nanmin(datos_sinErrores,axis=0)
print("media de cada columna",media_columna)

#cambiar promedio nan

for i in range(datos_sinErrores.shape[0]):
	for j in range(datos_sinErrores.shape[1]):
		if np.isnan(datos_sinErrores[i,j]):
			datos_sinErrores[i,j]=media_columna[j]

print("datos limpos",datos_sinErrores)




