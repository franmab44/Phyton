precio  = input("Introduce el precio del producto: ")
euros = precio.split(".")[0]
centimos = precio.split(".")[1]
print(f"El precio es euros = {euros}  con centimos = {centimos} ")