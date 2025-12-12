# lista_doble.py

# Clase NodoDoble
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.previo = None

# Clase ListaDoblementeEnlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None  # puntero a la cola para eficiencia

    # Insertar al inicio O(1)
    def insertar_al_inicio(self, nuevo_dato):
        nuevo_nodo = NodoDoble(nuevo_dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.previo = nuevo_nodo
            self.cabeza = nuevo_nodo
        print(f"Nodo insertado al inicio: {nuevo_dato}")

    # Insertar al final O(1) gracias al puntero cola
    def insertar_al_final(self, nuevo_dato):
        nuevo_nodo = NodoDoble(nuevo_dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.previo = self.cola
            self.cola = nuevo_nodo
        print(f"Nodo insertado al final: {nuevo_dato}")

    # Imprimir lista hacia adelante
    def imprimir_adelante(self):
        actual = self.cabeza
        print("Lista doble (adelante):")
        while actual is not None:
            print(f"{actual.dato} <-> ", end="")
            actual = actual.siguiente
        print("None")

    # Imprimir lista hacia atrás
    def imprimir_atras(self):
        actual = self.cola
        print("Lista doble (atrás):")
        while actual is not None:
            print(f"{actual.dato} <-> ", end="")
            actual = actual.previo
        print("None")
