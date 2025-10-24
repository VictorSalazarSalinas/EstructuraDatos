def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
numeros = [5, 2, 9, 1, 5, 6]
print("Lista ordenada:", burbuja(numeros))


