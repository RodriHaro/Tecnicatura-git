// Tipos de datos en JavaScript
/*
La sintaxis en lo que es comentarios es muy similar a la de Java, realmente diriamos que es la misma.
*/

let nombre = "Rodrigo"; // String
console.log(nombre); // Imprime el valor de la variable nombre
console.log(typeof nombre); // Imprime el tipo de dato de la variable nombre

nombre = 32; // Cambiamos el valor de la variable nombre a un número
console.log(typeof nombre); // Imprime el tipo de dato de la variable nombre (ahora es un número)

nombre = 12.5; // Cambiamos el valor de la variable nombre a un número decimal
console.log(typeof nombre); // Imprime el tipo de dato de la variable nombre (ahora es un número decimal)

let edad = 32; // Number
console.log(edad); // Imprime el valor de la variable edad

let objeto = { // Object
    nombre: "Rodrigo",
    edad: 32,
    email: "rodri.nh@gmail.com"
}
console.log(objeto); // Imprime el objeto completo
console.log(typeof objeto); // Imprime el tipo de dato de la variable objeto (es un objeto)

// Tipo de dato booleano
let bandera = true; // Boolean
console.log(bandera); // Imprime el valor de la variable bandera

//Tipo de dato funcion
function miFuncion() {} // Function
console.log(typeof miFuncion); // Imprime el tipo de dato de la variable miFuncion (es una función)

// Tipo de dato simbolo
let simbolo = Symbol("mi simbolo"); // Symbol
console.log(simbolo); // Imprime el valor de la variable simbolo (es un símbolo)
console.log(typeof simbolo); // Imprime el tipo de dato de la variable simbolo (es un símbolo)

// Tipo de dato clase
class Persona {
    constructor(nombre, apellido){
    this.nombre = nombre;
    this.apellido = apellido;
    }
} // Class
console.log(Persona); // Imprime la clase Persona (es una clase)
console.log(typeof Persona); // Imprime el tipo de dato de la variable Persona (es una clase pero la clase es una función)

// Tipo de dato undefined
let x; // Undefined
console.log(x); // Imprime el valor de la variable x (es undefined)
console.log(typeof x); // Imprime el tipo de dato de la variable x (es undefined)

x = undefined; // Asignamos el valor undefined a la variable x
console.log(x); // Imprime el valor de la variable x (es undefined)
console.log(typeof x); // Imprime el tipo de dato de la variable x (es undefined)

// null: significa ausencia de valor
let y = null; // Null no es un tipo de dato, pero su origen es un objeto
console.log(y); // Imprime el valor de la variable y (es null)
console.log(typeof y); // Imprime el tipo de dato de la variable y (es un objeto, pero es null)

// Tipo de dato array y empty string
let autos = ["Citroen","Audi", "BMW", "Ford"]; // Array
console.log(autos); // Imprime el array completo
console.log(typeof autos); // Imprime el tipo de dato de la variable autos (es un objeto, pero es un array)

let z = ""; // Empty string
console.log(z); // Imprime el valor de la variable z (es un string vacío)
console.log(typeof z); // Imprime el tipo de dato de la variable z (es un string vacío)