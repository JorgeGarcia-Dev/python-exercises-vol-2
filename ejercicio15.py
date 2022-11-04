"""
Define una función llamada adivina_numero. La función debe cumplir con los siguiente requerimientos.
La función no poseerá parámetro alguno.
La función elegirá un número aleatorio entre el 1 y el 100. La función preguntará al usuario que número se ha elegido.
Cada vez que el usuario ingrese un número la función imprimirá alguno de los siguientes mensajes
(Dependiendo cual sea el caso). Esto para darle una pista al usuario en su siguiente turno.
Más alto. Más bajo. Correcto.
Si el usuario responde incorrectamente en 3 ocasiones seguidas la función finalizará con el mensaje:
Lo sentimos, el número que estaba pensando es <Número>.
Si el usuario responde correctamente la función finalizará en ese momento.
"""

import random

def adivina_numero():

    numero_secreto = random.randint(1,100)

    intentos = 0

    while intentos < 3:

        numero_usuario = int(input("el número que creas es el número secreto: "))
        
        intentos = intentos + 1

        if numero_usuario < numero_secreto:
            print("Más alto.")

        if numero_usuario > numero_secreto:
            print("Más bajo.")

        if numero_usuario == numero_secreto:
            break

    if numero_usuario == numero_secreto:
        print("Correcto.")
    
    if numero_usuario != numero_secreto:
        print("Lo sentimos, el número que estaba pensando es", numero_secreto)

adivina_numero()