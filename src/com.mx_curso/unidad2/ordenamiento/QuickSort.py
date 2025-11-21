import random
# Lista de 200 puntuaciones
similaridades = [1,99,55,3]

# Función QuickSort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        mayores=[x for x in lista[1:] if x>pivote]
        print(mayores)
        menores=[x for x in lista[1:] if x<=pivote]
        print(mayores)
        return quicksort(mayores)+[pivote]+quicksort(menores)

# Ordenar de mayor a menor
resultado = quicksort(similaridades)

# Mostrar resultados
print("Lista de imágenes ordenadas por similaridad (mayor a menor):")
print(resultado)
