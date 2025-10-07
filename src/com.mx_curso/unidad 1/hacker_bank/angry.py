def angry(a,k):
	arrive=0
	for i in a:
		if i>=0:
			arrive+=1
	if arrive>=k:
		print("no")
	else:
		print("si")


k=3
a=[-2,-1,0,1,2]


angry(a,k)