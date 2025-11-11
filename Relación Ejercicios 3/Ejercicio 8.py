Valor = 2400

puntuacion = float(input("Introduce la puntuación del empleado: "))

nivel = ""
if puntuacion == 0.0:
    nivel = "Mal"
else:
    if puntuacion == 0.4:
        nivel = "Bien"
    else:
        if puntuacion >= 0.6:
            nivel = "Muy Bien"

cantidaddinero = Valor * puntuacion

print("Puntuación:", puntuacion)
print("Rendimiento:", nivel)
print("Cantidad a recibir:", cantidaddinero, "€")