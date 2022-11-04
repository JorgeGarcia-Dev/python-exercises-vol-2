"""
Desarrolla un programa que permita conocer si el primer y último elemento de una
lista son el mismo número.
"""

lista_numeros = [5,7,9,10,15,54,7]

def numeros_iguales():
    
    if lista_numeros[0] == lista_numeros[-1]:
        print(lista_numeros[0], "Es igual que", lista_numeros[-1])
    else:
        print(lista_numeros[0], "No es igual que", lista_numeros[-1])

numeros_iguales()