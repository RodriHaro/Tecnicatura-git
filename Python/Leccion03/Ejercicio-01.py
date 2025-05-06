# Preguntamos el nombre de la persona
nombre = input("Hola, ¿cómo es tu nombre?\n")

# Preguntamos cómo estuvo el día
dia = input(f"Hola {nombre}, ¿cómo estuvo tu día del 1 al 10?\n")

# Mostramos la respuesta
print(f"Mi día estuvo de: {int(dia)}")

# Evaluamos cómo estuvo el día y mensaje de despedida
if int(dia) >= 6:
    print("¡Me alegro que tu día haya estado bueno!")
else:
    print("Ya vendrán días mejores")