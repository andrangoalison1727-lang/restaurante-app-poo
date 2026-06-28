# Sistema de Gestión de Restaurante

**Nombre del estudiante:** Andrango Nieto Alison Dayana 

## Descripción del sistema

Este proyecto consiste en el desarrollo de un sistema básico de gestión para un restaurante utilizando Programación Orientada a Objetos (POO). El sistema permite registrar productos y clientes, almacenarlos en listas y mostrar su información en pantalla. Para ello, se implementaron clases, constructores, atributos y métodos que ayudan a organizar mejor el código.

## Estructura del proyecto

El proyecto está organizado en módulos para mantener una mejor organización del código.

```text
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
├── main.py
└── README.md
```

- **modelos/**: Contiene las clases `Producto` y `Cliente`.
- **servicios/**: Contiene la clase `Restaurante`, encargada de administrar los productos y clientes mediante listas y métodos para agregarlos y mostrarlos.
- **main.py**: Archivo principal donde se crean los objetos, se registran en el restaurante y se muestra la información.
- **README.md**: Documentación del proyecto.

## Tipos de datos utilizados

Se utilizaron diferentes tipos de datos según la información almacenada en el sistema:

- **str:** Para nombres, descripciones y números telefónicos.
- **int:** Para el número de mesa del cliente.
- **float:** Para el precio de los productos.
- **bool:** Para indicar si un producto está disponible.

## Reflexión sobre buenas prácticas

Durante el desarrollo del proyecto se utilizaron nombres claros para las clases, atributos y métodos, lo que facilita la lectura y comprensión del código. Además, dividir el programa en módulos permitió organizar mejor cada parte del sistema. El uso del método `__str__` hizo posible mostrar la información de los productos y clientes de una forma más clara, mientras que la clase `Restaurante` se encarga de administrar los registros, manteniendo el código más ordenado y fácil de mantener.