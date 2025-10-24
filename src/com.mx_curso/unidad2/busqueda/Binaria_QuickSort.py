import random

# Función QuickSort
def quicksort(lista):
    if len(lista)<=1:
        return lista
    else:
        pivote=lista[0]
        mayores=[x for x in lista[1:] if x>pivote]
        menores=[x for x in lista[1:] if x<=pivote]
        return quicksort(mayores)+[pivote]+quicksort(menores)

# Búsqueda binaria
def busqueda_binaria(lista,objetivo):
    inicio=0
    fin=len(lista)-1
    while inicio<=fin:
        medio=(inicio+fin)//2
        if lista[medio]==objetivo:
            return medio
        elif lista[medio]<objetivo:
            inicio=medio+1
        else:
            fin=medio-1
    return -1

# Lista aleatoria
clientes=[random.randint(1000, 9999) for _ in range(500)]
clientes_ordenados=quicksort(clientes)

# Mostrar lista ordenada (opcional)
#print(clientes_ordenados)

# Buscar un cliente
buscar=int(input("Ingrese el ID del cliente a buscar: "))
pos=busqueda_binaria(clientes_ordenados, buscar)

if pos != -1:
    print(f"Cliente encontrado en la posición {pos}")
else:
    print("Cliente no encontrado.")
