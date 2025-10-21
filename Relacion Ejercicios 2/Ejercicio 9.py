fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
partes = fecha.split("/")

dia = partes[0].zfill(2)
mes = partes[1].zfill(2)
anio = partes[2]

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")