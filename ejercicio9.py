"""
Desarrolla un programa que permita conocer el promedio de una lista de números enteros.
La función debe recibir como argumento una lista de longitud N de números enteros.
La función debe retornar en primedio de la lista.
"""

def validar_numeros(message):
    
    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")
            
def promedio():
    
    lista_numeros = []
    
    for n in range(10):
        num = validar_numeros("números aleatorios: ")
        lista_numeros.append(num)
    
    suma = sum(lista_numeros)
    longitud_de_lista = len(lista_numeros)
    resultado=suma/longitud_de_lista
    print(resultado)

promedio()