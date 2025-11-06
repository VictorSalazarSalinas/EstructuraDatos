# Lista con las calificaciones
importancias=[75,20,55,40,90,10,60,30]

print("Calificaciones no ordenadas")
print(importancias)

n=len(importancias)

for i in range(n):
    # Suponemos que el elemento i es el mayor
    maximo = i
    for j in range(i+1,n):
        if importancias[j]<importancias[maximo]:
            maximo=j
    # Intercambiar
    temp=importancias[i]
    importancias[i]=importancias[maximo]
    importancias[maximo]=temp

# Mostrar resultado
print("Calificaciones ordenadas por relevancia (menor a mayor):")
print(importancias)
