from random import randint

print('Bienvenidos al juego "Adivina el número". El juego consiste en adivinar el número antes de perder los 5 intentos.')
contador = 0
numero_aleatorio = randint(1, 10)

while contador < 5:
    numero_a_ingresar = int(input('Ingrese un número del 1 al 10: '))
    if numero_a_ingresar < numero_aleatorio:
        print('Ingresa un número más alto')
    elif numero_a_ingresar > numero_aleatorio:
        print('Ingresa un número más chico')
    elif numero_a_ingresar == numero_aleatorio:
        print(f'¡GANASTE! El número es: {numero_aleatorio}')
        seguir_jugando = input('¿Quieres seguir jugando? (si/no): ')
        if seguir_jugando.lower() == 'si':
            numero_aleatorio = randint(1, 10)  # Generar un nuevo número aleatorio
            contador = 0  # Reiniciar el contador de intentos
            continue
        else:
            print('¡Gracias por jugar!')
            break
    contador += 1

if contador == 5:
    print(f'¡Lo siento! Te has quedado sin intentos. El número era: {numero_aleatorio}')
