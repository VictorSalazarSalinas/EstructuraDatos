# Dos listas ordenadas
modelo1=[10,20,30,40,50,60,70,80,90,100]
modelo2=[15,25,35,45,55,65,75,85,95,105]

# Lista resultante
mezcla=[]

i=0
j=0

# Mezcla de las dos listas
while i<len(modelo1) and j<len(modelo2):
    if modelo1[i]<modelo2[j]:
        mezcla.append(modelo1[i])
        i+=1
    else:
        mezcla.append(modelo2[j])
        j+=1

# Agregar elementos restantes
while i<len(modelo1):
    mezcla.append(modelo1[i])
    i+=1

while j<len(modelo2):
    mezcla.append(modelo2[j])
    j+=1

# Mostrar lista final
print("Lista combinada de recomendaciones:")
print(mezcla)
