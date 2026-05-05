#---¡ADIVINA EL NÚMERO!---#
"""SE NECESITA CREAR UN JUEGO DE ADIVINANZA EN EL QUE EL USUARIO DEBE ADIVINAR UN NÚMERO ENTRE DISTINTAS DIFICULTADES (FACIL, NORMAL Y DIFICIL). EL PROGRAMA DEBE DAR PISTAS AL USUARIO SI EL NÚMERO ES DEMASIADO ALTO O DEMASIADO BAJO HASTA QUE ADIVINE CORRECTAMENTE. EL USUARIO TIENE UN NÚMERO LIMITADO DE INTENTOS (10 VIDAS), SI SE AGOTAN LAS VIDAS, EL PROGRAMA DEBE MOSTRAR EL NÚMERO CORRECTO Y TERMINAR EL JUEGO."""

import random

#Si se digita una letra, el programa se detiene, por lo que se recomienda ingresar un número para seleccionar la dificultad. Si se ingresa un número fuera del rango, se seleccionará la dificultad normal por defecto.#
while True:
    print("\n--- BIENVENIDO AL JUEGO DE ADIVINAR EL NÚMERO ---")
    print("Por favor, selecciona la dificultad: 1. Fácil (números del 1 al 10) | 2. Normal (números del 1 al 50) | 3. Difícil (números del 1 al 100)")
    dificultad = input("Ingrese el número de la dificultad (1-3): ")
    if dificultad == '1':
        numero_secreto = random.randint(1, 10)
    elif dificultad == '2':
        numero_secreto = random.randint(1, 50)
    elif dificultad == '3':
        numero_secreto = random.randint(1, 100)
    else:
        print("Dificultad inválida. Se seleccionará Normal.")
        numero_secreto = random.randint(1, 50)

#Si se digita una letra, el programa se detiene. Se recomienda ingresar un número para adivinar el número secreto. Si se ingresa un número fuera del rango, se restará una vida y se dará una pista.#
    vidas = 10
    rango_max = 10 if dificultad == '1' else 50 if dificultad == '2' else 100
    while vidas > 0:
        try:
            adivinanza = int(input("Adivina el número: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
            continue
        if adivinanza < 1 or adivinanza > rango_max:
            print("Número fuera de rango. Intenta de nuevo.")
            vidas -= 1
            print(f"Te quedan {vidas} vidas.")
            continue

        if adivinanza == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número {numero_secreto} correctamente. Te quedaron {vidas} vidas.")
            break

        elif abs(adivinanza - numero_secreto) <= 3:
            print("¡Muy cerca! Intenta de nuevo.")
            vidas -= 1
            print(f"Te quedan {vidas} vidas.")
        elif adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
            vidas -= 1
            print(f"Te quedan {vidas} vidas.")
        else:
            print("Demasiado alto. Intenta de nuevo.")
            vidas -= 1
            print(f"Te quedan {vidas} vidas.")

    if vidas == 0 and adivinanza != numero_secreto:
        print(f"¡Has perdido! El número correcto era {numero_secreto}.")

    jugar_nuevo = input("¿Deseas jugar de nuevo? (s/n): ")
    if jugar_nuevo == 'n':
        print("¡Gracias por jugar!")
        break
