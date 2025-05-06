# Ejercicio 3: Rango entre las edades 20 y 30 anios

edad = int(input("Escriba su edad: "))

veinte = edad >= 20 and edad < 30
print(veinte)

treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    if veinte:
        print(f"Estas dentro del rango de los 20")
    elif treinta:
        print(f"Estas dentro del rango de los 30")
else:
    print(f"Estas fuera del rango de los 20 a 30 anios")

# Otra forma de colocar el if
# if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
#     print(f"Estas dentro del rango de los 20 a 30 anios")

# Sintaxis simplificada del operador and
if 20 <= edad < 30 or 30 <= edad < 40:
    print(f"Estas dentro del rango de los 20 a 30 anios")
else:
    print(f"Estas fuera del rango de los 20 a 30 anios")