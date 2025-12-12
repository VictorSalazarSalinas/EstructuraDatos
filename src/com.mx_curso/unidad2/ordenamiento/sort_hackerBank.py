def ordenarBurbuja(a):
    n = len(a)
    numCambios = 0

    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  
                numCambios += 1

    print(f"El arreglo quedó ordenado con {numCambios} intercambios.")
    print(f"Primer elemento: {a[0]}")
    print(f"Último elemento: {a[-1]}")



arreglo =[5, 2, 9, 1, 5, 6]

ordenarBurbuja(arreglo)