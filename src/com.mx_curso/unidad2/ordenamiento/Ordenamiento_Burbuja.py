# Lista con las puntuaciones de riesgo de los correos
correos=[15,4,1,10]

print("Correos no ordenados:")
print(correos)


# Ordenamiento burbuja
n=len(correos)

for i in range(1):
    for j in range(n-i-1):
        if correos[j]>correos[j+1]:
            # Intercambiar los elementos
            temp=correos[j]
            correos[j]=correos[j+1]
            correos[j+1]=temp

# Mostrar la lista ordenada
print("Correos ordenados por riesgo (menor a mayor):")
print(correos)
