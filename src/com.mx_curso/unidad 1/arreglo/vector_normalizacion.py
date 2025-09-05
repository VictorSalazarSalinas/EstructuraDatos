#Detección de Colores en una Imagee

flor=[4.7,1.9,0.5]

flor_nor=[]

suma=sum(flor)

for x in flor:
	
	flor_nor.append(x/suma)

print(flor_nor)

