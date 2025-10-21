productos = input("Introduce los productos de la cesta de la compra separados por comas:")

listaproductos = productos.split(",")

print("\nProductos en la cesta:")
for producto in listaproductos:
    print(producto.strip()) 