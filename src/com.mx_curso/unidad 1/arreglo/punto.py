#Operación de producto punto (base de las redes neuronales)
 
import numpy as np
 
# Vector de entrada (una sola característica de 3 neuronas)
entrada = np.array([1, 2, 3])
 
# Matriz de pesos (3 neuronas de entrada, 2 de salida)
pesos = np.array([
    [0.5, 0.2],
    [0.8, 0.3],
    [0.1, 0.9]
])
 
# Realizar el producto punto
salida = np.dot(entrada, pesos)
print("Vector de entrada:", entrada)
print("Matriz de pesos:\n", pesos)
print("\nSalida de la capa de neuronas (producto punto):", salida)