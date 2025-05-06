# Ejercicio 5: Tienda de libros 

print("Escriba los siguientes datos del libro:")

nombre = input("Nombre del libro: ")
id = int(input("ID del libro: "))
precio = float(input("Precio del libro: "))
envioGratuito = input("Indicar si el envio es gratuito (si/no): ")

if envioGratuito == "si":
    envioGratuito = True
elif envioGratuito == "no":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir 'si' o 'no'"

print(f'''
      Nombre del libro: {nombre}
      ID del libro: {id}
      Precio del libro: {precio}
      Envio gratuito: {envioGratuito}
      ''')