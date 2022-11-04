"""
Define una función que permita reemplazar todas las vocales de un string por X.
La función debe recibir como argumento un string de longitud X.
La función debe imprimir en consola el nuevo string.
"""

def vocales_string():

    print('')
    cadena = input("Ingresa una frase que te motive: ")

    cadena_1 = cadena.replace('a', 'x')
    cadena_2 = cadena_1.replace('e', 'x')
    cadena_3 = cadena_2.replace('i', 'x')
    cadena_4 = cadena_3.replace('o', 'x')
    cadena_5 = cadena_4.replace('u', 'x')

    print(cadena_5)

vocales_string()