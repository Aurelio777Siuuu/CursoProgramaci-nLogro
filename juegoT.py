print("¡Bienvenido a la Exploración de Marte!")
print("Eres un astronauta en Marte. ¿Quieres explorar la cueva (1), el valle (2) o la meseta (3)?")
decision = input("Elige 1, 2 o 3: ")

if decision == '1':
    print("Encuentras cristales brillantes en la cueva.")
    print("¿Quieres recoger los cristales (1) o seguir explorando (2)?")
    sub_decision = input("Elige 1 o 2: ")
    if sub_decision == '1':
        print("¡Has recogido los cristales y regresaste a la nave con éxito!")
    elif sub_decision == '2':
        print("Sigues explorando y descubres un lago subterráneo.")
    else:
        print("Decisión no válida. ¡Intenta nuevamente!")

elif decision == '2':
    print("Descubres un antiguo artefacto en el valle.")
    print("¿Quieres investigar el artefacto (1) o seguir explorando (2)?")
    sub_decision = input("Elige 1 o 2: ")
    if sub_decision == '1':
        print("El artefacto resulta ser un mapa de Marte. ¡Increíble!")
    elif sub_decision == '2':
        print("Encuentras un grupo de rocas misteriosas.")
    else:
        print("Decisión no válida. ¡Intenta nuevamente!")

elif decision == '3':
    print("Llegas a la meseta y ves un paisaje impresionante.")
    print("¿Quieres tomar fotos (1) o investigar la flora (2)?")
    sub_decision = input("Elige 1 o 2: ")
    if sub_decision == '1':
        print("¡Las fotos son espectaculares! Capturas recuerdos de tu viaje.")
    elif sub_decision == '2':
        print("Descubres una planta que brilla en la oscuridad.")
    else:
        print("Decisión no válida. ¡Intenta nuevamente!")

else:
    print("Decisión no válida. ¡Intenta nuevamente!")