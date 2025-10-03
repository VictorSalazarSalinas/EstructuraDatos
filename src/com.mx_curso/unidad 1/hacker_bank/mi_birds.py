def mi_birds(arr):

	print(len(arr))
	print(arr)
	max_c=0

	for i in arr:
		print(i)
		max_b=arr.count(i)
		print(max_b)
		if max_b>max_c:
			posiscion=i
			max_c=max_b
			print(max_c)
			print("   ",posiscion)
	print(arr[posiscion-1])


arr=[1,4,4,4,5,3]
mi_birds(arr)