# Lista con las puntuaciones de riesgo de los correos
correos=[75,20,55,40,90,10,60,30,80,25]

print("Correos no ordenados:")
print(correos)


# Ordenamiento burbuja
n=len(correos)

for i in range(n-1):
    for j in range(n-i-1):
        if correos[j]>correos[j+1]:
            # Intercambiar los elementos
            temp=correos[j]
            correos[j]=correos[j+1]
            correos[j+1]=temp

# Mostrar la lista ordenada
print("Correos ordenados por riesgo (menor a mayor):")
print(correos)
