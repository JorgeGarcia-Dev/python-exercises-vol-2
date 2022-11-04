"""
Define una función que permita sumar 2 listas de números enteros. La función debe recibir como argumento 2 listas de longitud N.
La función debe retornar como resultado una nueva lista con el resultado de la suma de cada uno de los elementos en ambas listas.
"""

lista_1 = []
lista_2 = []
suma_de_listas = []

def validar_numeros(message):
    
    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

def lista_numeros():
    
    print('Lista 1')
    for n in range(5):
        numero = validar_numeros("Ios números a sumar en la primera lista: ")
        lista_1.append(numero)
    
    print('Lista 2')
    for n in range(5):
        numero = validar_numeros("los números a sumar en la segunda lista: ")
        lista_2.append(numero)
    
    for i in range(len(lista_1)):
        suma_de_listas.append(lista_1[i])
    
    for i in range(len(lista_2)):
        suma_de_listas[i] = suma_de_listas[i] + lista_2[i]

    print(suma_de_listas)

lista_numeros()