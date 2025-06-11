# Ejercicio 6
# Definimos las variables
n_elementos = int(input("Escriba la cantidad de elementos a ingresar: "))

i = 1
suma_pares = 0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0

# Bucle para ingresar números
while i <= n_elementos:
    num = int(input("Escriba un numero: "))
    
    # Verificar si es par o impar
    if num % 2 == 0:
        # El numero es par
        suma_pares = suma_pares + num
        conteo_pares = conteo_pares + 1
    else:
        # El numero es impar
        suma_impares = suma_impares + num
        conteo_impares = conteo_impares + 1
    
    # Incrementamos el contador
    i = i + 1

# Mostrar resultados
if conteo_pares > 0:
    print(f"La suma de los numeros pares es: {suma_pares}")
    print(f"El conteo de los numeros pares es: {conteo_pares}")
else:
    print("No se han escrito numeros pares")

if conteo_impares > 0:
    promedio_impares = suma_impares / conteo_impares
    print(f"El promedio de impares es: {promedio_impares}")
else:
    print("No se han escrito numeros impares")