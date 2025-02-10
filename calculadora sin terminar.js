//función de la calculadora
function calculadora() {
    const readline = require("readline");
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
mostrarMenu();
.question("Seleccione una opción: ", (opcion) => {if (opcion === "5") {
    consola.log("Hasta Luego!");
    rl.close();
    return;
}

rl.question("ingrese el primer número: ", (input1) => { const numero1 = parseFloat(input1);
rl.question("ingresa el segundo número: ", (input2) => const numero2 = parseFloat(input2);
const resultado = realizarOperacion(opcion, numero1 console.log("resultado: " + resultado);
rl.close();
console.log("¡Gracias por usar nuestra calculadora!, ¿en que te podemos ayudar?")