package Java.Ejercicio12;

import java.util.Scanner;

public class ejercicio12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese el valor de a: ");
        double a = scanner.nextDouble();
        
        System.out.print("Ingrese el valor de b: ");
        double b = scanner.nextDouble();
        
        // Aplicar la fórmula: (a+b)² = a² + b² + 2*a*b
        double cuadradoSuma = Math.pow(a, 2) + Math.pow(b, 2) + (2 * a * b);
        
        System.out.println("El resultado es: " + cuadradoSuma);
        
        scanner.close();
    }
}


