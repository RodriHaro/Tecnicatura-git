package Java.Ejercicio10;

import java.util.Scanner;

public class ejercicio10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        double num1, num2, resultado;

        System.out.print("Digite el primer numero: ");
        num1 = entrada.nextDouble();
        System.out.print("Digite el segundo numero: ");
        num2 = entrada.nextDouble();

        if (num1 == num2) {
            resultado = num1 * num2;
        } else if (num1 > num2) {
            resultado = num1 - num2;
        } else {
            resultado = num1 + num2;
        }

        System.out.println("El resultado es: " + resultado);
        entrada.close();
    }
}
