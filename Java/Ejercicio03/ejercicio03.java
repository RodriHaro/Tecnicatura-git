package Java.Ejercicio03;

import java.util.Scanner;

public class ejercicio03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Ingresa el largo: ");
        int largo = entrada.nextInt();
        
        System.out.print("Ingresa el ancho: ");
        int ancho = entrada.nextInt();
        
        double area = largo * ancho;
        double perimetro = 2 * (largo + ancho);
        
        System.out.println("Área: " + area);
        System.out.println("Perímetro: " + perimetro);

    }
}