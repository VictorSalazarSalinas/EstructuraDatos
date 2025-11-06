# Lista con las puntaciones
importancias=[75,20,55,40,90,10,60,30]

def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo  # Caso base: arreglo con 0 o 1 elemento
    pivote = arreglo[-1]  # Elegimos el último elemento como pivote
    menores = [x for x in arreglo[:-1] if x <= pivote]  
    mayores = [x for x in arreglo[:-1] if x > pivote] 
      
    # Aplicamos recursión y combinamos resultados

    return quicksort(menores) + [pivote] + quicksort(mayores)

resultado = quicksort(importancias)

# Mostrar resultado
print("puntaciones ordenadas (menor a mayor):")
print(resultado)
