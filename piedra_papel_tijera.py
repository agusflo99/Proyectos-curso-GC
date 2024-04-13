from random import randint

while True:
        print('Hola Bienvenidos al juego del Piedra,papel o Tijera')
        eleccion= input('Elige piedra, papel o tijera: ')
        eleccion_jugador = eleccion.lower()
        opcion_aleatoria = randint(1,3)
        if opcion_aleatoria == 1:
            print('Piedra')
            if eleccion_jugador == 'piedra' and opcion_aleatoria == 1:
                print('EMPATE')
            elif eleccion_jugador =='tijera' and opcion_aleatoria == 1:
                print('PERDISTE')
            elif eleccion_jugador =='papel' and opcion_aleatoria == 1:
                print('GANASTE')
        elif opcion_aleatoria == 2:
            print('Papel')
            if eleccion_jugador == 'piedra' and opcion_aleatoria == 2:
                print('PERDISTE')
            elif eleccion_jugador =='tijera' and opcion_aleatoria == 2:
                print('GANASTE')
            elif eleccion_jugador =='papel' and opcion_aleatoria == 2:
                print('EMPATE')
        elif opcion_aleatoria == 3:
            print('Tijera')
            if eleccion_jugador == 'piedra' and opcion_aleatoria == 3:
                print('GANASTE')
            elif eleccion_jugador =='tijera' and opcion_aleatoria == 3:
                print('EMPATE')
            elif eleccion_jugador =='papel' and opcion_aleatoria == 3:
                print('PERDISTE')
        seguir_jugando = input('¿Quieres volver a jugar?: ')
        respuesta = seguir_jugando.lower()
        if respuesta == 'si':
            continue
        else:
            print('Gracias por jugar')
            break



