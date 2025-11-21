# Lista ordenada de lecturas
lecturas=[5,8,1,3,2]

# Nueva lectura del sensor
#nueva_lectura = int(input("Ingrese la nueva lectura del sensor: "))

# Agregar la nueva lectura al final
#lecturas.append(nueva_lectura)

# Ordenar usando inserción
for i in range(1,len(lecturas)):
    valor=lecturas[i]
    j=i-1
    print(j)
    while j>=0 and lecturas[j]>valor:
        lecturas[j+1]=lecturas[j]
        j-=1
    lecturas[j+1]=valor
    print(lecturas,valor)

# Mostrar lista actualizada
print("Lista actualizada de lecturas ordenadas:")
print(lecturas)
