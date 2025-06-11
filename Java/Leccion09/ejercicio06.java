package Java.Leccion09;

import java.util.Scanner;

public class ejercicio06 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo,luis,juan,total;
        System.out.println("Escriba la cantidad de dinero que tiene Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());

        luis = guillermo / 2;
        juan = (guillermo + luis) / 2;

        total = guillermo + luis + juan;
        System.out.println("El dinero de Luis es: " + luis);
        System.out.println("El dinero de Juan es: " + juan);
        System.out.println("El dinero total de los tres es: US$" + total);

        entrada.close();
    }
}
