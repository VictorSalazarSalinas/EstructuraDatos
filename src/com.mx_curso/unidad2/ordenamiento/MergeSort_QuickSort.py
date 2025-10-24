import random
import time

# MergeSort
def merge_sort(lista):
    if len(lista)<=1:
        return lista
    medio=len(lista)//2
    izquierda=merge_sort(lista[:medio])
    derecha=merge_sort(lista[medio:])
    
    resultado=[]
    i=j=0
    while i<len(izquierda) and j<len(derecha):
        if izquierda[i]<derecha[j]:
            resultado.append(izquierda[i])
            i+=1
        else:
            resultado.append(derecha[j])
            j+=1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Función QuickSort
def quicksort(lista):
    if len(lista)<=1:
        return lista
    else:
        pivote=lista[0]
        mayores=[x for x in lista[1:] if x>pivote]
        menores=[x for x in lista[1:] if x<=pivote]
        return quicksort(mayores)+[pivote]+quicksort(menores)

# Tamaños a probar
tamaños=[1000,10000]
for tamaño in tamaños:
    print(f"\nProbando con {tamaño} elementos:")

    datos=[random.randint(0,10000) for _ in range(tamaño)]

    # MergeSort
    inicio=time.time()
    merge_sort(datos.copy())
    fin=time.time()
    print(f"MergeSort: {fin-inicio:.4f} segundos")

    # QuickSort
    inicio=time.time()
    quicksort(datos.copy())
    fin=time.time()
    print(f"QuickSort: {fin-inicio:.4f} segundos")
