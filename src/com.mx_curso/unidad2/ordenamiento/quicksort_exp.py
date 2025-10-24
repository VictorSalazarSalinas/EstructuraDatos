def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo  # Caso base: arreglo con 0 o 1 elemento
    pivote = arreglo[-1]  # Elegimos el último elemento como pivote
    menores = [x for x in arreglo[:-1] if x <= pivote]  
    mayores = [x for x in arreglo[:-1] if x > pivote] 
      
    # Aplicamos recursión y combinamos resultados
    return quicksort(menores) + [pivote] + quicksort(mayores)

# Ejemplo de uso
arreglo = [8, 3, 1, 7, 0, 10, 2]
print("Arreglo ordenado: ", quicksort(arreglo))