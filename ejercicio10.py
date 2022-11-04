"""
Define una función que permita conocer si un valor es único dentro de una lista.
La función debe recibir 2 argumento, una lista de longitud N y el valor a buscar dentro de la lista.
La función debe retornar verdadero o falso si el valor es único dentro de la lista.
"""

lista_numeros = []
nueva_lista = []

def validar_numeros(message):
    
    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

def numeros():

    for n in range(5):
        numero = validar_numeros("un número: ")
        lista_numeros.append(numero)
        
    no_repetido = min(set(lista_numeros), key = lista_numeros.count)
    
    numero = validar_numeros("el número  a buscar: ")
    
    if numero == no_repetido:
        print("Éste valor es único dentro de la lista.")
    else:
        print("Éste valor se repida y no es único.")

numeros()