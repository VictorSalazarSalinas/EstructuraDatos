# Lista ordenada de lecturas
lecturas=[22,35,47,51,60]

# Nueva lectura del sensor
nueva_lectura = int(input("Ingrese la nueva lectura del sensor: "))

# Agregar la nueva lectura al final
lecturas.append(nueva_lectura)

# Ordenar usando inserción
for i in range(1,len(lecturas)):
    valor=lecturas[i]
    j=i-1
    while j>=0 and lecturas[j]>valor:
        lecturas[j+1]=lecturas[j]
        j-=1
    lecturas[j+1]=valor

# Mostrar lista actualizada
print("Lista actualizada de lecturas ordenadas:")
print(lecturas)
