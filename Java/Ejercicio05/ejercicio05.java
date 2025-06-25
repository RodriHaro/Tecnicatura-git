package Java.Ejercicio05;

import java.util.Scanner;

public class ejercicio05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float nota1,nota2,nota3,suma;

        //Guardamos las notas
        System.out.println("Escriba las tres calificaciones: ");
        nota1 = Float.parseFloat(entrada.nextLine());
        nota2 = Float.parseFloat(entrada.nextLine());
        nota3 = Float.parseFloat(entrada.nextLine());

        suma = nota1 + nota2 + nota3;

        System.out.println("La suma de las tres calificaciones es: " + suma);

    }
}


