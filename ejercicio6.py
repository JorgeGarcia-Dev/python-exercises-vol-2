"""
Define una función que permita sumar 101 a cada uno de los elementos de una lista.
La función debe recibir como argumento una listas de longitud N.
La función debe imprimir en consola el resultado de la operación.
"""

lista_numeros = []

def validar_numeros(message):
    
    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

def lista():
    
    for n in range(10):
        n = validar_numeros("Ingresa los números a sumar: ")
        numero = n + 101
        lista_numeros.append(numero)

lista()

print(lista_numeros)