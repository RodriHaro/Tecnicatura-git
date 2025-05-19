# Ejercicio 5: Sistema de Calificaciones

calificacion = float(input("Ingrese una calificación del 0 al 10: "))

if 9 <= calificacion <= 10:
    print("A")
elif 8 <= calificacion < 9:
    print("B")
elif 7 <= calificacion < 8:
    print("C")
elif 6 <= calificacion < 7:
    print("D")
elif 0 <= calificacion < 6:
    print("F")
else:
    print("El valor ingresado es incorrecto")
