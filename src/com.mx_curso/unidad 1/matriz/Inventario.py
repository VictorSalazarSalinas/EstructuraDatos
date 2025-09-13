# Inventario: ID Cantidad Precio
inventario = [
    [1, 50, 20.5],
    [2, 30, 15.0],
    [3, 80, 10.0]
]


print("ID  Stock  Precio")
for producto in inventario:
    print(producto[0],"  ",producto[1],"  " ,producto[2])

# Elegimos el producto con ID 2
producto = inventario[1]
valor_total = producto[1] * producto[2]
print("Valor total del producto 2: $",valor_total)

# Venta de 10 unidades
producto[1] -= 10
print("Stock actualizado del producto 2: ",producto[1])
