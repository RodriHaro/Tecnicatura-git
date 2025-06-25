package Java.Ejercicio01.EjercicioLibroAutor;
import java.util.Scanner;

public class LibroAutor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hola! como es tu nombre?: ");
        var nombre = scanner.nextLine();

        System.out.println("Hola " + nombre + ", ingresa el nombre del libro: ");
        var nombreLibro = scanner.nextLine();

        System.out.println("Ahora ingresa el nombre del autor: ");
        var nombreAutor = scanner.nextLine();

        System.out.println(nombreLibro + " fue escrito por " + nombreAutor);

        scanner.close();
    }
}