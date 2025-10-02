dias= ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"] 
ventas=[] 
# Ingreso de ventas 
for dia in dias: 
	valor=float(input(f"Ventas del {dia}: ")) 
	ventas.append(valor) 
# Cálculos 
total=sum(ventas) 
mayor=max(ventas) 
menor=min(ventas) 
dia_mayor=dias[ventas.index(mayor)] 
dia_menor=dias[ventas.index(menor)] 
# Resultados 
print(f"\nTotal de ventas: {total}") 
print(f"Día con más ventas: {dia_mayor} ({mayor})") 
print(f"Día con menos ventas: {dia_menor} ({menor})") 
