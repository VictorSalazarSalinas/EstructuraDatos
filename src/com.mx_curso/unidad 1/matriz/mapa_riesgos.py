matriz=[
	[0,1,2,1,2,0,1,1],
	[0,1,2,1,2,0,1,1],
	[0,1,2,1,2,0,1,1],
	[0,1,2,1,2,0,1,1],
	[0,1,2,1,2,0,1,1],
	[0,1,2,1,2,0,1,1],
	[0,1,2,1,2,0,1,1]
]




for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print()



area_riesgo=0
areas_preucacion=0

for f in range(len(matriz)):
	for j in range(len(matriz[f])):
		print(matriz[f][j], end="")
		if matriz[f][j]==2:
			area_riesgo+=1
		if matriz[f][j]==1:
			areas_preucacion+=1
	print()

print(f"area de riesgo (2):{area_riesgo} ")
print(f"area de preucacion (1): {areas_preucacion}")


print("actualizacion de preucacion")


for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		if matriz[i][j]==2:
			matriz[i][j]=1
	
		



area_riesgo_act=0
areas_preucacion_act=0


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
        if matriz[i][j] == 2:
            area_riesgo_act += 1
        if matriz[i][j] == 1:
            areas_preucacion_act += 1
    print()

print(f"Área de riesgo actualizada: {area_riesgo_act}")
print(f"Área de precaución actualizada: {areas_preucacion_act}")
