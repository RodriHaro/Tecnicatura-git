# Ejercicio 1: Calcular la suma de "N" primeros numeros

try:
    # Definir N
    N = int(input("Escriba la cantidad de numeros a sumar: "))
    
    if N <= 0:
        print("Error: Debe ingresar un numero positivo")
        exit()
    
    # Iniciar suma
    suma = 0
    
    # Ciclo para sumar los primeros N numeros
    i = 1
    while i <= N:
        suma = suma + i
        i = i + 1
    
    # Mostrar resultado
    print(f"\nLa suma de los primeros {N} numeros es: {suma}")
        
except ValueError:
    print("Error: Por favor ingrese un numero entero valido")
