def count_A_O(s,t,a,b,m,n,apples,oranges):
	r_a=0
	r_o=0
	for i in apples:
		z=i
		z=z+a
		print(z)
		if z>=7 and z<=10:
			r_a+=1
			
	for i in oranges:
		z=i
		z=z+b
		print(z)
		if z>=7 and z<=10:
			r_o+=1

	print("casa de sam rango inicia :",s," termina :",t)
	print("posiscion arbol de manzanas :",a," naranjas: ",b)
	print("numero de manzanas :",m," numero de naranjas :",n)
	print("posiscion de las manzanas :",apples," posiscion de las naranjas :",oranges)
	print("manzanas rango :",r_a," naranjas rango: ",r_o)
	
s=7
t=10
a=4
b=12
m=3
n=3
apples=[2,3,-4]
oranges=[3,-2,-4]

count_A_O(s,t,a,b,m,n,apples,oranges)