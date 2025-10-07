ahorros = float(input("¿Dinero ahorrado?:"))
intereses = float(4/100)
Calculo1 = ((ahorros*intereses)*12)
Calculo2 = ((ahorros*intereses)*12)*2
Calculo3 = ((ahorros*intereses)*12)*3
total1 = round(Calculo1,2)
total2 = round(Calculo2,2)
total3 = round(Calculo3,2)
print(f"Los ahorros que tendras en 1 año son: {total1}€")
print(f"Los ahorros que tendras en 2 años son: {total2}€")
print(f"Los ahorros que tendras en 3 años son: {total3}€")