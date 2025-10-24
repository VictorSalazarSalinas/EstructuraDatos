import random
# Lista de 200 puntuaciones
similaridades = [random.randint(0, 1000) for _ in range(200)]

# Función QuickSort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        mayores=[x for x in lista[1:] if x>pivote]
        menores=[x for x in lista[1:] if x<=pivote]
        return quicksort(mayores)+[pivote]+quicksort(menores)

# Ordenar de mayor a menor
resultado = quicksort(similaridades)

# Mostrar resultados
print("Lista de imágenes ordenadas por similaridad (mayor a menor):")
print(resultado)
