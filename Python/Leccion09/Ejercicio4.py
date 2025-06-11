# Ejercicio 4: Suponga que se tiene un conjunto de calificaciones de un
# grupo de 10 alumnos. Realizar un algoritmo para calcular la
# calificacion promedio y la calificacion mas baja de todo el grupo

# Definir variables
calificacion_promedio = 0
calificacion_baja = 99999  

# Definir i y suma
i = 1
suma = 0

# Ciclo para leer 10 calificaciones
while i <= 10:
    try:
        calificacion = float(input(f"Escriba la calificacion del alumno {i}: "))
        
        # Suma de las calificaciones
        suma = suma + calificacion
        
        # Calcular la menor calificacion
        if calificacion < calificacion_baja:
            calificacion_baja = calificacion
        
        i = i + 1
        
    except ValueError:
        print("Error: Por favor ingrese una calificacion valida (numero)")
        continue

# Calcular promedio
calificacion_promedio = suma / 10

# Mostrar resultados
print("RESULTADOS:")
print(f"La calificacion promedio es: {calificacion_promedio:.2f}")
print(f"La calificacion mas baja es: {calificacion_baja:.2f}")
