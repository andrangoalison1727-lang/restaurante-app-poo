class Producto:

    # 1. Constructor de la clase Producto
    def __init__(self, nombre: str, descripcion: str, precio: float, disponible: bool):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.disponible = disponible

    # 2. Mostrar información del producto
    def __str__(self) -> str:
        return f"Producto: {self.nombre}, Descripción: {self.descripcion}, Precio: {self.precio}, Disponible: {self.disponible}"