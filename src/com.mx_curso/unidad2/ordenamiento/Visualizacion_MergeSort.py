def merge_sort_visual(lista, nivel=0):
    # Imprimir el estado actual de la lista
    indent = "  " * nivel  # Espacios para mostrar niveles
    print(f"{indent}Dividir: {lista}")

    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = merge_sort_visual(lista[:mitad], nivel + 1)
    derecha = merge_sort_visual(lista[mitad:], nivel + 1)

    # Mezclar las dos mitades ordenadas
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    print(f"{indent}Mezclar: {resultado}")
    return resultado

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

# Lista de ejemplo (8 elementos)
lista_original=[42,17,8,99,23,11,55,3]

# Ejecutar y visualizar el ordenamiento
print("Visualización del algoritmo MergeSort:\n")
merge_sort_visual(lista_original)
