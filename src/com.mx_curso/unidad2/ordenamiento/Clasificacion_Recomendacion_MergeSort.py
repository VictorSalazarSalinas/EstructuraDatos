import random

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

# Crear lista de 100 puntuaciones de productos
productos=[random.randint(0,100) for _ in range(100)]

# Ordenar
ordenados=merge_sort(productos)
print(ordenados)
# Mostrar top 5
print("Top 5 productos recomendados:")
for i in range(5):
    print(f"Producto {i+1}: Puntuación {ordenados.pop()}")
