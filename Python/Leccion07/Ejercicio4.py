# Ejercicio 4: Etapas de Vida

edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("La edad no puede ser negativa.")
elif 0 <= edad <= 10:
    print("La infancia es increíble y bella.")
elif 11 <= edad <= 19:
    print("Tienes muchos cambios, mucho que estudiar.")
elif 20 <= edad <= 29:
    print("Amor y comienza el trabajo.")
elif 30 <= edad <= 39:
    print("Etapa de crecimiento profesional y personal.")
elif 40 <= edad <= 59:
    print("Madurez, experiencia y consolidación.")
elif 60 <= edad <= 79:
    print("Disfrutar de la jubilación y la familia.")
elif edad >= 80:
    print("Sabiduría y legado para las nuevas generaciones.")
else:
    print("Edad fuera de rango")
