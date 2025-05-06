# Ejercicio 1: Valor dentro de un rango

valor = int(input("Escriba un numero dentro del rango de 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and valor <= valorMaximo

if dentroRango:
    print(f"El valor {valor} está dentro del rango")
else:
    print(f"El valor {valor} está fuera del rango")
