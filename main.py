    # 1. Importaciones

from modelos.producto import Producto
from modelos.cliente import Cliente 
from servicios.restaurante import Restaurante

def main():
    # 2. Objeto principal del sistema
    mi_restaurante = Restaurante()

    # 3. Creación de productos
    producto1 = Producto("Fideos Wonton", "Fideos chinos rellenos de carne y verduras", 8.99, True)
    producto2 = Producto("Mousse de Chocolate", "Postre de chocolate con crema batida", 6.99, True)
    producto3 = Producto("Salmón a la Plancha", "Filete de salmón fresco con salsa de limón", 14.99, True)
    producto4 = Producto("Ensalada César", "Lechuga, pollo a la parrilla y crutones", 10.99, True)
    producto5 = Producto("Cheesecake", "Delicioso cheesecake con frutos rojos", 7.99, True)

    # 4. Creación de clientes
    cliente1 = Cliente("Israel", 1, "055-1234567")
    cliente2 = Cliente("Natalia", 2, "044-9876543")
    cliente3 = Cliente("Clara", 3, "066-7654321")
    cliente4 = Cliente("Faz", 4, "077-3456789")
    cliente5 = Cliente("Fransheskha", 5, "088-5678901")

    # 5. Agregando productos y clientes al restaurante
    mi_restaurante.agregar_producto(producto1)
    mi_restaurante.agregar_producto(producto2)
    mi_restaurante.agregar_producto(producto3)
    mi_restaurante.agregar_producto(producto4)
    mi_restaurante.agregar_producto(producto5)

    mi_restaurante.agregar_cliente(cliente1)
    mi_restaurante.agregar_cliente(cliente2)
    mi_restaurante.agregar_cliente(cliente3)
    mi_restaurante.agregar_cliente(cliente4)
    mi_restaurante.agregar_cliente(cliente5)

    # 6. Visualización

    print("=== SISTEMA DE ADMINISTRACIÓN DE RESTAURANTE ===\n")
    mi_restaurante.mostrar_productos()
    print("\n") 
    mi_restaurante.mostrar_clientes()

# 7. Ejecutar el sistema
if __name__ == "__main__":
    main()