def mi_birds(arr):

	print(len(arr))
	print(arr)
	max_c=0
	z=0
	indice=[]
	for i in arr:		
		
		max_b=arr.count(i)
		print(max_b)
		if max_b>max_c:
			if max_b>max_c:
				indice.clear()
				indice.append(z)
			else:
				indice.append(z)
			posiscion=z
			max_c=max_b
			print(max_c)
			print("   ",posiscion)
		z=z+1
	
	#indice.pop(0)
	print(indice)
	print(arr[min(indice)])
	
	
arr=[1,4,4,2,2,3,3,7,7,7]
mi_birds(arr)