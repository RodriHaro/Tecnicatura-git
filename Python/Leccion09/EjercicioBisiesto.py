# Ejercicio Año Bisiesto: Determinar si un año es bisiesto

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

while True:
    try:
        # Solicitar el año al usuario
        num = int(input("Ingrese el año: "))
        
        # Verificar si es bisiesto
        if es_bisiesto(num):
            print(f"El año {num} es Bisiesto")
        else:
            print(f"El año {num} no es Bisiesto")
        
        # Preguntar si desea continuar
        print("\nPara seguir adelante escriba la opcion 1:")
        opcion = input("Opcion: ")
        
        # Si no es 1, terminar el programa
        if opcion != "1":
            print("Gracias por usar el programa!")
            break
        
    except ValueError:
        print("Error: Por favor ingrese un año valido")
        continue

