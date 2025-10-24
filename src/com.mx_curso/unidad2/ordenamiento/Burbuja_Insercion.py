import random
import time

# Función de ordenamiento burbuja
def burbuja(lista):
    n=len(lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]

# Función de ordenamiento por inserción
def insercion(lista):
    for i in range(1,len(lista)):
        valor=lista[i]
        j=i-1
        while j>=0 and lista[j]>valor:
            lista[j+1]=lista[j]
            j-=1
        lista[j+1]=valor

# Tamaños a probar
tamaños=[100,1000,10000]

for tamaño in tamaños:
    print(f"\nProbando con {tamaño} elementos:")

    # Crear lista aleatoria
    datos=[random.randint(0,10000) for _ in range(tamaño)]

    # Burbuja
    lista_burbuja=datos.copy()
    inicio=time.time()
    burbuja(lista_burbuja)
    fin=time.time()
    print(f"Burbuja: {fin-inicio:.4f} segundos")

    # Inserción
    lista_insercion=datos.copy()
    inicio=time.time()
    insercion(lista_insercion)
    fin=time.time()
    print(f"Inserción: {fin-inicio:.4f} segundos")
