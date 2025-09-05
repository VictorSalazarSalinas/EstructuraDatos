# Matriz de calificaciones
calificaciones = [
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4]
]

# Imprimir la matriz
for x in calificaciones:
    print(x)

# Calcular promedio de una película específica
pelicula_index=int(input("Ingresa el índice de la película(0 a 3): "))

suma=0
contador=0
for usuario in calificaciones:
    suma+=usuario[pelicula_index]
    contador+=1


promedio = suma / contador
print(f"Promedio de calificaciones de la película {pelicula_index}: {promedio:.2f}")


# Mostrar las calificaciones de un usuario específico
usuario_index = int(input("Ingresa el índice del usuario (0 a 3): "))
print(f"Calificaciones del usuario {usuario_index}: {calificaciones[usuario_index]}")
