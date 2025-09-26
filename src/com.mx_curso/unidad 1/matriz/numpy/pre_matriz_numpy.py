import numpy as np

# Crear un mapa de riesgo 8x8 con valores aleatorios entre 0 y 2
np.random.seed(0)  # para que el resultado sea el mismo cada vez
mapa=np.random.randint(0,3.size=(8,8))

# Mostrar mapa original
print("Mapa de Riesgo (0=Seguro, 1=Precaución, 2=Alto Riesgo):")
print(mapa)

# Contar zonas de precaución (1) y alto riesgo (2)
precaucion=0
alto_riesgo=0

for i in range(mapa.shape[0]):       # recorrer filas
    for j in range(mapa.shape[1]):   # recorrer columnas
        if mapa[i][j]==1:
            precaucion+=1
        elif mapa[i][j]==2:
            alto_riesgo+=1

# Reemplazar los valores 2 por 1 manualmente con bucles
for i in range(mapa.shape[0]):
    for j in range(mapa.shape[1]):
        if mapa[i][j]==2:
            mapa[i][j]=1  # convertir alto riesgo en precaución

# Mostrar resultados
print(f"\nZonas de precaución: {precaucion}")
print(f"Zonas de alto riesgo (antes de actualizar): {alto_riesgo}")

# Mapa actualizado
print("\nMapa actualizado:")
print(mapa)
