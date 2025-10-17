import numpy as np


#cargar el dataset
datos = np.genfromtxt(r'C:\Users\victo\Desktop\tareas\datos\ESTRUCUTURADATOS\src\com.mx_curso\unidad 1\matriz\numpy\processed.cleveland.data', delimiter=',', dtype='object')


print(datos)

import numpy as np

datos_l = np.genfromtxt(r'C:\Users\victo\Desktop\tareas\datos\ESTRUCUTURADATOS\src\com.mx_curso\unidad 1\matriz\numpy\processed.cleveland.data',
    delimiter=',',    
    dtype=float
)


print(datos_l)




datos_l[0,0]=np.nan
datos_l[1,2]=np.nan


print(datos_l)
#
#
#


media_columna=np.nanmin(datos_l,axis=0)
print("media de cada columna",media_columna)
#
##cambiar promedio nan
#
for i in range(datos_l.shape[0]):
	for j in range(datos_l.shape[1]):
		if np.isnan(datos_l[i,j]):
			datos_l[i,j]=media_columna[j]

print("datos limpos",datos_l)#


mediana=np.median(datos_l,axis=0)
des=np.std(datos_l,axis=0)

print("medidas de tendencia central")
print(media_columna)
print(mediana)
print(des)


col_indice=4

print("promedio de colesterol",media_columna[col_indice])


pre_indice=3
num_pre_ma_promedio=0

for i in range(datos_l.shape[0]):
	if datos_l[i,pre_indice]>media_columna[pre_indice]:
			num_pre_ma_promedio=num_pre_ma_promedio+1

print("porcentaje de pacientes con presión arterial mayor al promedio",num_pre_ma_promedio)


mayor_fre_indice=7
mayor_fre=0
edad=0

for i in range(datos_l.shape[0]):
	if datos_l[i,mayor_fre_indice]>mayor_fre:
		mayor_fre=datos_l[i,mayor_fre_indice]
		edad=datos_l[i,0]

print("edad del paciente con la mayor frecuencia cardiaca alcanzada ",edad," frecuencia ",mayor_fre)
		
