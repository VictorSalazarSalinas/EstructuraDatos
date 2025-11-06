def merge_sort(lista):
    if len(lista) <= 1:
        return lista  # Caso base

    # 1. Dividir
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    # 2. Mezclar
    return mezclar(izquierda, derecha)

def mezclar(izquierda, derecha):
    resultado = []
    i = j = 0

    # Comparar y mezclar
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Ejemplo de uso
numeros = [38, 27, 43, 3, 9, 82, 10]
ordenados = merge_sort(numeros)
print(ordenados)
