package Java.Ejercicio04;

import java.util.Scanner;

public class ejercicio04 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Ingresa el primer número: ");
        int num1 = entrada.nextInt();
        
        System.out.print("Ingresa el segundo número: ");
        int num2 = entrada.nextInt();
        
        int mayor = (num1 > num2) ? num1 : num2;
        
        System.out.println("El mayor es: " + mayor);
        
    }
}       

