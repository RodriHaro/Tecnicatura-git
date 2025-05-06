# Ejercicio 1: Numero par o impar

a = int(input("Escriba un numero: "))
print(f"El numero residuo de la division es: {a % 2}")

if a % 2 == 0:
    print(f"El valor de a es: {a} y es par")
else:
    print(f"El valor de a es: {a} y es impar")

