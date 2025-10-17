import numpy as np


#cargar el dataset
datos = np.genfromtxt(r'C:\Users\victo\Desktop\tareas\datos\ESTRUCUTURADATOS\src\com.mx_curso\unidad 1\matriz\numpy\practica_numpy_1\iris.data', delimiter=',', dtype='object')


print(datos)

import numpy as np

datos_numericos = np.genfromtxt(r'C:\Users\victo\Desktop\tareas\datos\ESTRUCUTURADATOS\src\com.mx_curso\unidad 1\matriz\numpy\practica_numpy_1\iris.data',
    delimiter=',',
    usecols=[0, 1, 2, 3],
    dtype=float
)


print(datos_numericos)

indices_eliminar=[0,1,2,50]

datos_limpos=np.delete(datos_numericos,indices_eliminar,axis=0)


print("datos limpos",datos_limpos)


datos_limpos[0,0]=np.nan
datos_limpos[1,2]=np.nan
datos_limpos[2,2]=np.nan
datos_limpos[2,1]=np.nan
datos_limpos[2,1]=np.nan
datos_limpos[3,0]=np.nan
datos_limpos[2,1]=np.nan
datos_limpos[2,1]=np.nan
datos_limpos[2,1]=np.nan
datos_limpos[0,0]=np.nan



print(datos_limpos)



ultimafila=datos_limpos[0] -1
print("ultima fila",ultimafila)

media_columna=np.nanmin(datos_limpos,axis=0)
print("media de cada columna",media_columna)

#cambiar promedio nan

for i in range(datos_limpos.shape[0]):
	for j in range(datos_limpos.shape[1]):
		if np.isnan(datos_limpos[i,j]):
			datos_limpos[i,j]=media_columna[j]

print("datos limpos",datos_limpos)