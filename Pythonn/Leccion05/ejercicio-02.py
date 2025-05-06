# Ejercicio 2: Operador or y not
# Usamos el operador or y not para determinar si puede asistir al juego, al colocar not el resultado se invierte.

vacaciones = True
diaDeDescanso = True

if not vacaciones or diaDeDescanso:
    print("Tiene trabajo que hacer")
else:
    print("Puede asistir al juego")