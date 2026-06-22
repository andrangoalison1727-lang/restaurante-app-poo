class Producto: 
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio  

    def __str__(self):
        return f"Producto: {self.nombre}, descripcion: {self.descripcion}, precio: {self.precio}"