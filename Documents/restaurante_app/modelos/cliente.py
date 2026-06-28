class Cliente:

    # 1. Constructor de la clase Cliente

    def __init__(self, nombre: str, mesa: int, telefono: str):
        self.nombre = nombre
        self.mesa = mesa
        self.telefono = telefono
    
    # 2. Mostrar información del cliente
    def __str__(self)-> str:
        return f"Cliente: {self.nombre}, Mesa: {self.mesa}, Teléfono: {self.telefono}"