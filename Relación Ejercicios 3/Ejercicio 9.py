edad = int(input("¿Edad? "))

if edad < 4:
    print("Gratis.")
elif edad <= 18:
    print("5€")
else:
    print("10€")