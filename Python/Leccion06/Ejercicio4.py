# Ejercicio 4:

# Área y longitud de un circulo
# Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia.
# Área = Pi * r2
# Longitud = 2 * Pi * r

import math

# Pedimos al usuario el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calculamos el área
area = math.pi * radio ** 2

# Calculamos la longitud de la circunferencia
longitud = 2 * math.pi * radio

# Mostramos los resultados
print(f"El área del círculo es: {area}")
print(f"La longitud de la circunferencia es: {longitud}")