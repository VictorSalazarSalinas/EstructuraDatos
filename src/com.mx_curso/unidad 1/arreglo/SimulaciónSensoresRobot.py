# Lecturas de los sensores

lecturas=[120,85,210,150]
umbral=100


for i in range(len(lecturas)):


    print(f"Sensor {i + 1}: {lecturas[i]} cm")


    if lecturas[i]<umbral:
        

        print("Advertencia")
