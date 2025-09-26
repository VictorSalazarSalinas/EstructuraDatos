# Vector de características de una flor
caracteristicas = [3.5, 1.4, 0.2]

# Suma total
suma = sum(caracteristicas)

# Normalización
normalizadas = []
for valor in caracteristicas:
    normalizadas.append(valor / suma)

# Mostrar resultados
print("Vector normalizado:")
for i, val in enumerate(normalizadas):
    print(f"Característica {i+1}: {val}")
