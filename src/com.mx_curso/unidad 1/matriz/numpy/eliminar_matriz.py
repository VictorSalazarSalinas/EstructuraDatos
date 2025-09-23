import numpy as np


#creacion de una matriz 3X3



datos=np.array([
                [10,20,30,40],
                [15,25,35,45],
                [25,20,45,55]


	])


print("---conjunto de datos original---")
print(datos)




datos_limpios=np.delete(datos,2,axis=0)

print("----datos limpos--")
print(datos_limpios)


datos_limpios2=np.delete(datos_limpios,0,axis=1)

print("----datos limpos 2--")
print(datos_limpios2)




