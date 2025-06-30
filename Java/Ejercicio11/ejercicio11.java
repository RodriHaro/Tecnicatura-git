// Ejercicio 1: Convertir horas totales a semanas, días y horas

package Java.Ejercicio11;

import java.util.Scanner;

public class ejercicio11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese el total de horas: ");
        int totalHoras = scanner.nextInt();
        
        // Calcular semanas (1 semana = 168 horas)
        int semanas = totalHoras / 168;
        int horasRestantes = totalHoras % 168;
        
        // Calcular días (1 día = 24 horas)
        int dias = horasRestantes / 24;
        int horas = horasRestantes % 24;
        
        System.out.println("Resultado: " + semanas + " semanas, " + dias + " días y " + horas + " horas");
        
        scanner.close();
    }
}  
