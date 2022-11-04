"""
Define una función que permita eliminar todos los valores duplicados en una lista.
La función debe recibir como argumento una lista de longitud N.
La función debe retornar una nueva lista sin valores duplicados.
"""

def validar_numeros(message):
    
    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

def numeros_repetidos():
    
    lista_numeros = []
    
    nueva_lista = []
    
    for n in range(10):
        numero = validar_numeros("un número: ")
        lista_numeros.append(numero)
    
    for n in lista_numeros:
        if n not in nueva_lista:
            nueva_lista.append(n)
    print(nueva_lista)

numeros_repetidos()