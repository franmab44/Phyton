usuario = float(input("Introduce tu renta anual: "))
if usuario < 10000:
    print("Tipo imositivo 5")
elif 10000 <= usuario < 20000:
    print("Tipo imositivo 15")
elif 20000 <= usuario < 35000:
    print("Tipo imositivo 20")
elif 35000 <= usuario < 60000:
    print("Tipo imositivo 30")
else: 
    print("Tipo imositivo 45")