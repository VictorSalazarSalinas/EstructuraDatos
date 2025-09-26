import numpy as np

# Matriz de pesos (3 entradas x 2 salidas)
pesos=np.array([
    [0.2,0.8],
    [0.5,0.1],
    [0.9,0.3]
])

# Vector de entrada
entrada=np.array([1.0,2.0,3.0])

# Producto punto: entrada (1x3) * pesos (3x2) = salida (1x2)
salida=np.dot(entrada, pesos)

# Mostrar resultados
print("Valores de salida:")
for i, val in enumerate(salida):
    print(f"Salida {i+1}: {val}")
