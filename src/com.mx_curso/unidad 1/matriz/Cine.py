#Crear mapa 4x5 con asientos libres
cine = [[1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1],
                        ]

# Mostrar mapa de asientos
print("Mapa de Asientos (0=Libre,1=Ocupado):")
for fila in cine:
    print(fila)

# Reservar asiento
fila=int(input("Elige la fila (0-3): "))
columna=int(input("Elige el asiento (0-4): "))

if cine[fila][columna]==0:
    cine[fila][columna]=1
    print("reservado")
else:
    print("ocupado")
libres=0
#mapa actualizado
for fila in cine:
    #contar
    for x in fila:
        if x==0:
            libres+=1
    print(fila)



print("Asientos libres: ", libres )
