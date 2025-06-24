package Java.CondicionalEjercicio2;

import java.util.Scanner;

public class CondicionalEjercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Escriba un numero de mes: ");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "Estacion desconocida";
        switch (mes) {
            case 1, 2, 3 -> estacion = "Verano";
            case 4, 5, 6 -> estacion = "Otoño";
            case 7, 8, 9 -> estacion = "Invierno";
            case 10, 11, 12 -> estacion = "Primavera";
        }
        System.out.println("La estacion es: " + estacion);
    }
}
