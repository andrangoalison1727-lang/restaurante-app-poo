#Importacion de clases
from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante

#Crear clientes

mi_cliente1 = Cliente("Israel", 1, "055-1234567")
mi_cliente2 = Cliente("Natalia", 2, "044-9876543")
mi_cliente3 = Cliente("Clara", 3, "066-7654321")
mi_cliente4 = Cliente("Faz", 4, "077-3456789")
mi_cliente5 = Cliente("Fransheskha", 5, "088-5678901")

#Crear productos

mi_producto1 = Producto("fideos wonton", "Fideos chinos rellenos de carne y verduras, servidos en caldo", 8.99)
mi_producto2 = Producto("Mousse de Chocolate", "Postre de chocolate con crema batida", 6.99)
mi_producto3 = Producto("Salmón a la Plancha", "Filete de salmón fresco a la plancha con salsa de limón", 14.99)
mi_producto4 = Producto("Ensalada César", "Ensalada fresca con lechuga, pollo a la parrilla, crutones y aderezo César", 10.99)
mi_producto5 = Producto("Cheesecake de Frutos Rojos", "Delicioso cheesecake con una mezcla de frutos rojos frescos", 7.99)

#Agregar clientes y productos al restaurante
#clientes
mi_restaurante = Restaurante()
mi_restaurante.agregar_cliente(mi_cliente1)
mi_restaurante.agregar_cliente(mi_cliente2)
mi_restaurante.agregar_cliente(mi_cliente3)
mi_restaurante.agregar_cliente(mi_cliente4)
mi_restaurante.agregar_cliente(mi_cliente5)
#productos
mi_restaurante.agregar_producto(mi_producto1)
mi_restaurante.agregar_producto(mi_producto2)
mi_restaurante.agregar_producto(mi_producto3)
mi_restaurante.agregar_producto(mi_producto4)
mi_restaurante.agregar_producto(mi_producto5)

#Mostrar clientes y productos
print("Clientes:")
mi_restaurante.mostrar_clientes()
print("\nProductos:")
mi_restaurante.mostrar_producto()
