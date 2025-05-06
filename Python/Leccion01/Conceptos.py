## Conceptos de todas las lecciones

unaVariable = 1

print(unaVariable)

unaVariable = "hola"
print(unaVariable)


x = 1
y = 2
z = x + y
print(z)


## para saber donde se encuentra guardada la variable en memoria
print(id(x))
print(id(y))
print(id(z))


# Tipos de datos en Python
# En Python no es necesario declarar el tipo de dato, ya que lo infiere automáticamente

# int
a = 10
print(type(a)) # para saber el tipo de dato que es se coloca type antes de la variable

# float
b = 10.5
print(type(b))

# bool
c = True # Tiene que ser con la primera letra en mayúscula
print(type(c))

# str
d = "Hola"  # Tiene que ser con comillas dobles o simples
print(type(d))


# Manejo de cadenas

# Concatenación de cadenas 1
miGrupoFavorito = "Pearl Jam"+" y " + "Alice in Chains"
print("Mi grupo favorito es: " + miGrupoFavorito)


# Concatenación de cadenas 2
cadena1 = "Hola"
cadena2 = "Mundo"
cadena3 = cadena1 + " " + cadena2
print(cadena3)

# Concatenación de cadenas 3
miGrupoFavorito = "Pearl Jam"
miGrupoFavorito2 = "Alice in Chains"
print("Mi grupo favorito es: " , miGrupoFavorito , " y " , miGrupoFavorito2)


# Convertir cadenas a enteros
numero1 = "10"
numero2 = "20"
print(int(numero1) + int(numero2)) # Para convertir a entero se usa int()

# Booleanos
miBooleano = 3 > 2
print(miBooleano) 

if miBooleano:
    print("Es verdadero")
else:
    print("Es falso")

# Procesar entrada del usuario - funcion input()

resultado = input("¿Cuál es tu nombre?")  # input() siempre devuelve un string, por lo que si se quiere convertir a otro tipo de dato, se debe hacer explícitamente
print(resultado)

numero3 = int(input("Escriba el primer número: "))
numero4 = int(input("Escriba el segundo número: "))
suma = numero3 + numero4
print("El resultado de la suma es: " , suma) 
print(f"El resultado de la suma es: {suma}") 

resta = numero3 - numero4
print(f"El resultado de la resta es: {resta}")

multiplicacion = numero3 * numero4
print(f"El resultado de la multiplicación es: {multiplicacion}")   

division = numero3 / numero4
print(f"El resultado de la división es: {division}")

divisionEntera = numero3 // numero4
print(f"El resultado de la división entera es: {divisionEntera}")   

modulo = numero3 % numero4
print(f"El resultado del módulo es: {modulo}")

exponente = numero3 ** numero4
print(f"El resultado del exponente es: {exponente}")

# Operadores de reasignación +=, -=, *=, /=, //=, %=, **=
# Se usa para reasignar el valor de una variable, es decir, se le suma, resta, multiplica, divide, etc. el valor de la variable a sí misma

numero5 = 10
numero5 += 5 # numero5 = numero5 + 5
print(f"El resultado de la suma es: {numero5}")

numero5 -= 5 # numero5 = numero5 - 5
print(f"El resultado de la resta es: {numero5}")

numero5 *= 5 # numero5 = numero5 * 5
print(f"El resultado de la multiplicación es: {numero5}")

numero5 /= 5 # numero5 = numero5 / 5
print(f"El resultado de la división es: {numero5}")

# Operadores de comparación ==, !=, >, <, >=, <=
# Se usan para comparar dos valores y devolver un valor booleano (True o False)

a = 10
b = 20
resultado = a == b # True si son iguales, False si son diferentes
print(resultado) # True si son iguales, False si son diferentes

resultado = a != b # True si son diferentes, False si son iguales
print(resultado) # True si son diferentes, False si son iguales

resultado = a > b # True si a es mayor que b, False si no
print(resultado) # True si a es mayor que b, False si no

resultado = a < b # True si a es menor que b, False si no
print(resultado) # True si a es menor que b, False si no

resultado = a >= b # True si a es mayor o igual que b, False si no
print(resultado) # True si a es mayor o igual que b, False si no

resultado = a <= b # True si a es menor o igual que b, False si no
print(resultado) # True si a es menor o igual que b, False si no

# Operadores lógicos and, or, not
# Se usan para combinar dos o más condiciones y devolver un valor booleano (True o False)

a = True
b = True
resultado = a and b # True si ambas son verdaderas, False si alguna es falsa
print(resultado)
resultado = a or b # True si alguna es verdadera, False si ambas son falsas
print(resultado)
resultado = not a # True si a es falsa, False si a es verdadera
print(resultado)




