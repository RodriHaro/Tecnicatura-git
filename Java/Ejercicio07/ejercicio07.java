package Java.Ejercicio07;

import java.util.Scanner;

public class ejercicio07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        final int salario = 1000;
        int comision = 150, venta;
        float salarioMensual, ventaCarro, porcVenta, totalPrecio;

        System.out.println("Escriba el numero de carros vendidos: ");
        venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Escriba el precio de cada carro: ");
        ventaCarro = Float.parseFloat(entrada.nextLine());

        comision *= venta;
        totalPrecio = ventaCarro * venta;
        porcVenta = totalPrecio * 0.05f;
        salarioMensual = salario + comision + porcVenta;

        System.out.println("El salario mensual es: " + salarioMensual);

        entrada.close();
    }
}
