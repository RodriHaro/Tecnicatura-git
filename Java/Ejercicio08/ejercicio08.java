package Java.Ejercicio08;

import java.util.Scanner; 


public class ejercicio08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        double nota1, nota2, nota3, promedio;

        // Solicitar las 3 calificaciones
        System.out.print("Digite la primera calificación: ");
        nota1 = entrada.nextDouble();
        System.out.print("Digite la segunda calificación: ");
        nota2 = entrada.nextDouble();
        System.out.print("Digite la tercera calificación: ");
        nota3 = entrada.nextDouble();

        // Calcular el promedio
        promedio = (nota1 + nota2 + nota3) / 3;

        // Verificar si aprueba o no
        if (promedio >= 70) {
            System.out.println("El alumno está aprobado con: " + promedio);
        } else {
            System.out.println("El alumno está desaprobado con: " + promedio);
        }
        entrada.close();
    }
}
