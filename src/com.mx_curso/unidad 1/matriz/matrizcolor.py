#Detección de Colores en una Imagee
matriz = [
    [[0, 0, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
]

a=0
v=0
r=0

matrizv=[0,1,0]
matriza=[0,0,1]
matrizr=[1,0,0]

#contar

for x in matriz:
	for y in x:
		if y==matriza:
			a=a+1
		if y==matrizv:
			v=v+1
		if y==matrizr:
			r=r+1
				

print(a,v,r)
