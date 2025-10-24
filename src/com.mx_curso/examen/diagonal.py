def diagonal(a):
	sumd1=0
	sumd2=0
	u=0
	
	#diagonal 1
	for x in a:

		i=0
		#print(u)
		for z in x:
			if i==u:
				#print(u)
				sumd1=sumd1+z
			i=i+1
		u=u+1
	
	u=len(a)
	u=u-1

	#diagonal 2
	for x in a:
		i=0
		#print(u)
		for z in x:
			if i==u:
				#print(u)
				sumd2=sumd2+z
			i=i+1
		u=u-1
	
	print(sumd1-sumd2)
		
a=[ [1,2,3],
	[4,5,6],
	[7,8,9]]


diagonal(a)