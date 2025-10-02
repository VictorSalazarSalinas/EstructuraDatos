# Matriz de calificaciones (usuarios x películas)
calificaciones [
    [4,5,3],
    [2,4,4],
    [5,5,5]
]

# Mostrar la matriz
print("Matriz de calificaciones:")
for fila in calificaciones:
    print(fila)

# Promedio de una película (columna)
pelicula=int(input("\nIngrese el índice de la película (0-2): "))
suma=0
for fila in calificaciones:
    suma+=fila[pelicula]
promedio=suma/len(calificaciones)
print(f"Promedio de la película {pelicula}: {promedio}")

# Mostrar calificaciones de un usuario
usuario=int(input("\nIngrese el índice del usuario (0-2): "))
print(f"Calificaciones del usuario {usuario}: {calificaciones[usuario]}")
