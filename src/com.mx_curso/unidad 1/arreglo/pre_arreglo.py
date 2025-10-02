# Lista para guardar precisiones 
precisiones=[] 
print("Ingrese las precisiones del modelo (escriba 'fin' para terminar):") 
while True: 
	entrada=input("Precisión: ") 
	if entrada.lower()=='fin': 
		break 
	try: 
		valor=float(entrada) 
		precisiones.append(valor) 
	except ValueError: 
	print("Por favor, ingrese un número válido.") 
if precisiones: 
	print(f"\nPrecisión final: {precisiones[-1]}") 
	print(f"Precisión más alta: {max(precisiones)}") 
else: 
	print("No se ingresaron precisiones.") 