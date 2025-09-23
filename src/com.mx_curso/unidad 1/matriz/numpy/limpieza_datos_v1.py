import numpy as np

np.random.seed(42)

datos=np.random.rand(5,5)*100


datos[2,3]=-999
datos[4,1]=150

print(datos)

indices_error=[2,4]

datos_limpios=np.delete(datos,indices_error,axis=0)
print()
print(datos_limpios)



