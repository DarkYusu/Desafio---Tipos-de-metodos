import random
from personaje import Personaje

def main():
    # Dar la bienvenida al jugador y solicitar el nombre para su personaje
    print("¡Bienvenido a Gran Fantasía!")
    nombre_jugador = input("Por favor indique nombre de su personaje: ")
    jugador = Personaje(nombre_jugador)
    orco = Personaje("Orco")

    # Crear el personaje del jugador y mostrar su estado en pantalla
    print(jugador.obtener_estado())
    print("¡Oh no!, ¡Ha aparecido un Orco!")

    while True:
        # Crear un personaje “Orco” y calcular la probabilidad de ganar que tiene el personaje del jugador versus el orco
        probabilidad = jugador.probabilidad_ganar(orco)
        opcion = Personaje.dialogo_enfrentamiento(probabilidad)
        
        if opcion == 2:
            # Si el jugador ha decidido huir, mostrar mensaje en pantalla informando que el orco ha quedado atrás
            print("¡Has huido! El orco ha quedado atrás.")
            break
        
        # Mientras la opción de juego del usuario sea “Atacar” (1), se debe realizar lo siguiente:
        resultado = random.uniform(0, 1)
        if resultado <= probabilidad:
            # Obtener el resultado del ataque del jugador al orco (Gana)
            print("¡Le has ganado al orco, felicidades!")
            jugador.asignar_estado(50)
            orco.asignar_estado(-30)
        else:
            # Obtener el resultado del ataque del jugador al orco (Pierde)
            print("¡Oh no! ¡El orco te ha ganado!")
            jugador.asignar_estado(-30)
            orco.asignar_estado(50)

        # Informar al jugador el resultado del ataque, los puntos de experiencia ganados o perdidos según corresponda
        print(jugador.obtener_estado())
        print(orco.obtener_estado())

        # Con el estado modificado, actualizar el valor de probabilidad de ganar al orco
        probabilidad = jugador.probabilidad_ganar(orco)
        
        # Volver a consultar al jugador su opción de juego
        if jugador.nivel == 1 and jugador.experiencia == 0 and opcion == 1:
            print("No puedes seguir luchando, has perdido toda tu experiencia.")
            break

if __name__ == "__main__":
    main()