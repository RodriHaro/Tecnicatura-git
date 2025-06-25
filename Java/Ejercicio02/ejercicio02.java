package Java.Ejercicio02;

import java.util.Scanner;

public class ejercicio02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese los siguientes datos del libro:");
        System.out.print("Digite el nombre del libro: ");
        String nombre = scanner.nextLine();
        System.out.print("Digite el ID del libro: ");
        String id = scanner.nextLine();
        System.out.print("Digite el precio del libro: ");
        double precio = scanner.nextDouble();
        System.out.print("Indique si el envío es gratuito (true/false): ");
        boolean envioGratuito = scanner.nextBoolean();
        System.out.println("\n--- Datos del libro ---");
        System.out.println("Nombre: " + nombre);
        System.out.println("ID: " + id);
        System.out.println("Precio: " + precio);
        System.out.println("Envío Gratuito?: " + envioGratuito);
    }
}
