"""
A partir de 2 listas de números enteros, define una función que imprima en consola
todos los números que se encuentren repetidos en ambas listas.
La función debe recibir como argumentos 2 listas de longitud N.
"""

lista_a = []
lista_b = []

def validar_numeros(message):
    
    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

def listas():

    for n in range(5):
        numero_a = validar_numeros("un número para la lista_a: ")
        lista_a.append(numero_a)

    for n in range(5):
        numero_b = validar_numeros("un número para la lista_b: ")
        lista_b.append(numero_b)

    print("Los números repetidos en ambas listas son: \n")
    
    for i in range(5):
        if lista_a[i] in lista_b:
            print(lista_a[i])

listas()