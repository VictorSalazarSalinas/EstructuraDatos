tablero=[] 
print("Ingrese los valores del tablero (0 = vacío, 1 = obstáculo):") 
for i in range(5): 
	fila=[] 
	for j in range(5): 
		valor=int(input(f"Celda ({i},{j}): ")) 
		fila.append(valor) 
	tablero.append(fila) 
# Mostrar el tablero 
print("\nTablero:") 
for fila in tablero: 
	print(fila) 
# Contar obstáculos totales 
total_obstaculos=sum([fila.count(1) for fila in tablero]) 
print(f"\nTotal de obstáculos: {total_obstaculos}") 
# Obstáculos en fila específica 
fila_usuario=int(input("Ingrese el número de fila (0-4) para contar obstáculos: ")) 
obstaculos_fila=tablero[fila_usuario].count(1) 
print(f"Obstáculos en la fila {fila_usuario}: {obstaculos_fila}") 
