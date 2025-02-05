print("===bienvenido al pepito's supermarket===")

comida = []
precio = []

while True:
    print("==¿Qué quieres hacer?==")
    print("1. agregar nuevo producto")
    print("2. mostrar el contenido en la cesta de compras")
    print("3. eliminar un elemento de la cesta de compras")
    print("4. dejar carrito e irse a casa")
    
    decision = input("Elige 1, 2, 3 o 4:")
    if decision == "1":
       nombre = input("¿qué quieres poner en la cesta?")
       comida.append(nombre)
       print("\nse agregò tu producto")
       
    elif decision == "2":
       if len(comida) == 0:
           print("la cesta está vacía")
       
       else:
           print("en tu cesta hay:")
           for i in range(len(comida)):
               print(f"(i+1). {comida[i]} - \n")
    elif decision == "3":
        if len(comida) == 0:
            print(" tu cesta está vacía")
        else:
            numero = int(input("¿qué quieres quitar de la cesta?")
            index = numero - 1
            comida.pop(index)
            precio.pop(index)
            print("listo rey ya se quitó")
    elif decision == "4":
        else print("pepe")
    
    
    
    break
