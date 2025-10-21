producto =  input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
numerounidades = int(input("Introduce el numero de unidades: "))

total = precio * numerounidades

print(f"{producto}: precio unitario {precio:8.2f}, unidades {numerounidades:3d}, coste total {total:10.2f}")