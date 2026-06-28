from modelos.producto import Producto
from modelos.cliente import Cliente 

class Restaurante:
    # 1. Constructor de la clase Restaurante
    def __init__(self):
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto: Producto)-> None:
        self.productos.append(producto)

    def agregar_cliente(self, cliente: Cliente)-> None:
        self.clientes.append(cliente)

    # 2. Mostrar información de los productos

    def mostrar_productos(self)-> None:
        print("=== LISTA DE PRODUCTOS ===")
        for producto in self.productos:
            print(producto)


# 3. Mostrar información de los clientes

    def mostrar_clientes(self)-> None:
        print("\n=== LISTA DE CLIENTES ===")
        for cliente in self.clientes:
            print(cliente)