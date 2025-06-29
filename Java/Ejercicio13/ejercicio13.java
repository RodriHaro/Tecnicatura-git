package Java.Ejercicio13;

import java.util.Scanner;

public class ejercicio13 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese la calificación de participación: ");
        double participacion = scanner.nextDouble();
        
        System.out.print("Ingrese la calificación del primer examen parcial: ");
        double primerParcial = scanner.nextDouble();
        
        System.out.print("Ingrese la calificación del segundo examen parcial: ");
        double segundoParcial = scanner.nextDouble();
        
        System.out.print("Ingrese la calificación del examen final: ");
        double examenFinal = scanner.nextDouble();
        
        // Participación: 10%, Primer parcial: 25%, Segundo parcial: 25%, Final: 40%
        double calificacionFinal = (participacion * 0.10) + 
                                  (primerParcial * 0.25) + 
                                  (segundoParcial * 0.25) + 
                                  (examenFinal * 0.40);
        
        System.out.println("Calificación final: " + String.format("%.2f", calificacionFinal));
        
        scanner.close();
    }
}    