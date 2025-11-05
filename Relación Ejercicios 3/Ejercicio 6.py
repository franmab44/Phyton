nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M para mujer, H para hombre): ")
nombre = nombre.upper()
sexo = sexo.upper()
if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

print(f"Tu grupo es el {grupo}.")