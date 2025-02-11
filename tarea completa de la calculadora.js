// Función para mostrar el menú bicho ese
function mostrarMenu() {
    console.log("1. Sumar");
    console.log("2. Restar");
    console.log("3. Multiplicar");
    console.log("4. Dividir");
    console.log("5. Salir");
}

// Función para realizar la operación seleccionada
function realizarOperacion(opcion, numero1, numero2) {
    switch (opcion) {
        case '1':
            return sumar(numero1, numero2);
        case '2':
            return restar(numero1, numero2);
        case '3':
            return multiplicar(numero1, numero2);
        case '4':
            return dividir(numero1, numero2);
        default:
            return 'Operación no válida';
    }
}

// Funciones de operaciones aritméticas
function sumar(a, b) {
    return a + b;
}

function restar(a, b) {
    return a - b;
}

function multiplicar(a, b) {
    return a * b;
}

function dividir(a, b) {
    if (b === 0) {
        return 'No se puede dividir por cero';
    }
    return a / b;
}

// Función principal de la calculadora
function calculadora() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    mostrarMenu();

    rl.question("Seleccione una opción: ", (opcion) => {
        if (opcion === '5') {
            console.log("Un placer ayudarle caballero");
            rl.close();
            return;
        }

        rl.question("Ingrese el primer número: ", (input1) => {
            const numero1 = parseFloat(input1);

            rl.question("Ingrese el segundo número: ", (input2) => {
                const numero2 = parseFloat(input2);

                const resultado = realizarOperacion(opcion, numero1, numero2);
                console.log("Resultado: " + resultado);

                rl.close();
            });
        });
    });
}

// Ejecutar la calculadora
calculadora();
