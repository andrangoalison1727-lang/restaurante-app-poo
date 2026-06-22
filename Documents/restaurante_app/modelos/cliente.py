class Cliente:
    def __init__(self, nombre, mesa, telefono):
        self.nombre = nombre
        self.mesa = mesa
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, mesa: {self.mesa}, telefono: {self.telefono}"
    