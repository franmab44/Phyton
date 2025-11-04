usuario = input("Introduzca tu edad: ")
ingresos = input("Introduzca sus ingresos mensuales: ") 
if  usuario >= "16" and float(ingresos) >= 1000:
    print("Puede tributar")
else:
    print("No puede tributar")