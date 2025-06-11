# Ejercicio 3: Leer 10 números e imprimir cuantos son positivos,
# cuantos negativos y cuantos neutros (Diagrama N-S)

# Definir contadores
conteo_positivos = 0
conteo_negativos = 0
conteo_neutros = 0
    
    # Definir i 
i = 1
    
    # Ciclo para leer 10 numeros
while i <= 10:
        try:
            num = float(input(f"Escriba el numero {i}: "))
            
            # Verificar si es positivo, negativo o neutro
            if num > 0:
                conteo_positivos = conteo_positivos + 1
            elif num < 0:
                conteo_negativos = conteo_negativos + 1
            else:  # num == 0
                conteo_neutros = conteo_neutros + 1
            
            i = i + 1
            
        except ValueError:
            print("Error: Por favor ingrese un numero valido")
            continue
    
    # Mostrar resultados
print("RESULTADOS:")
print(f"La cantidad de positivos es: {conteo_positivos}")
print(f"La cantidad de negativos es: {conteo_negativos}")
print(f"La cantidad de neutros es: {conteo_neutros}")
