
# Manipulación de un vector de características
mod=0
suma=0
con=0
persona=[0,0,0]


for i in range(len(persona)):
	mod=int(input("Que elemento desea modificar 1-altura 2-peso 3-edad :"))
	print("\n")
	
	mod=mod-1
	
	print(mod)


	cam=int(input("modificacion :"))

	persona[mod]=cam

	prin(cam)

for i in range(len(persona)):
	suma=persona[i]+suma
	con=con+1

promedio=suma/con

print("promedio final :")

print(promedio)


