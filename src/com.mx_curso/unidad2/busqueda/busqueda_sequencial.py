
def busqueda_secuencial(arr,a):
	for i in range(len(arr)):
		if arr[i]==a:
			return 1
	return -1
	

if __name__=="__main__":
	datos=[0,1]
	elemnto=0
	indice=busqueda_secuencial(datos,elemnto)
	if indice==1:
		print("elemnto {elemnto} encontrado en la indice {indice}")
	else:
		print("no encontrado")
