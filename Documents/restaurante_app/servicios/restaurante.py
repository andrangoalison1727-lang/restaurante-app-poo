from modelos.cliente import Cliente
from modelos.producto import Producto

class Restaurante:
    def __init__(self):
        self.cliente = []
        self.producto = []
#Agregar clientes y productos al restaurante

    def agregar_cliente(self,cliente):
        self.cliente.append(cliente)
    
    def agregar_producto(self,producto):
        self.producto.append(producto)
        
#Mostrar clientes y productos
        
    def mostrar_clientes(self):
        for cliente in self.cliente:
            print(cliente)
    def mostrar_producto(self):
        for producto in self.producto:
            print(producto)
    