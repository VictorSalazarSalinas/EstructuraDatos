#priorizacion de alertas de un sistema de detecion de fraudes

import numpy as np

np.random.seed(42)

datos=np.random.rand(10)

print(datos)


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        mayores=[x for x in lista[1:] if x>pivote]
        menores=[x for x in lista[1:] if x<=pivote]
        return quicksort(mayores)+[pivote]+quicksort(menores)

# Ordenar de mayor a menor
resultado = quicksort(datos)

# Mostrar resultados
print("Lista de mayor a menor:")
print(resultado)
