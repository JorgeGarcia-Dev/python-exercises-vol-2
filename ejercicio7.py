"""
Define un función que permita conocer si un valor se encuentra dentro de una lista.
La función debe recibir como argumento 2 valores, una lista de longitud N y el valor a buscar dentro de la lista.
La función debe retornar verdadero o falso si el valor a buscar se encuentra dentro de la lista.
"""

def validar_numeros(message):
    
    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

def buscar_numero():
    
    lista_numeros = []
    
    for n in range(5):
        numero = validar_numeros("una serie de números: ")
        lista_numeros.append(numero)
    for n in lista_numeros:
        num = int(input("Ingresa el número que deseas buscar: "))
        if num in lista_numeros:
            return True
        else:
            return False

print(buscar_numero())