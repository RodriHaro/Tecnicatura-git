# Ejercicio 7: 

# Definimos las variables
i = 1
suma = 0

# Bucle para procesar los 5 empleados
while i <= 5:
    print(f"--- Empleado {i} ---")
    
    # Solicitamos las horas trabajadas
    horas = float(input("Escriba las horas trabajadas: "))
    
    # Solicitamos la tarifa por hora
    tarifa = float(input("Escriba la tarifa por hora: $"))
    
    # Calculamos el salario
    salario = horas * tarifa
    
    # Mostramos el salario del empleado
    print(f"El salario es: ${salario:.2f}")
    
    # Sumar al total
    suma = suma + salario
    i = i + 1
    
    print()  # Linea en blanco

# Mostramos el resultado de la suma de los salarios
print(f"La suma de todos los salarios es: ${suma:.2f}")