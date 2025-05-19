# Determinar la solución lógica de la siguiente operación.

a = 10
b = 20

# Primero resolvemos las operaciones entre paréntesis:
# 3 + 5 * 8 = 3 + 40 = 43
# 43 < 3 = False

# -6 / 3 * 4 = -2 * 4 = -8
# -8 + 2 = -6
# -6 < 2 = True

# False and True = False
# 10 > 20 = False
# False or False = False

resultado = ((3 + 5 * 8) < 3 and ((-6 / 3 * 4) + 2 < 2)) or (a > b)
print(f"El resultado de la expresión es: {resultado}")






