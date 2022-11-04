"""
Define una función que permita conocer la cantidad de vocales dentro de un string.
La función debe recibir como argumento un string de longitud X.
La función debe imprimir en consola la cantidad de vocales existente dentro del string.
"""

def vocales_string():
    print('')
    cadena = input("Ingresa una frase que te motive: ")
    nueva_cadena = []
    
    for c in cadena:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            nueva_cadena.append(c)
    print('')        
    print("Las vocales que se encontraron son: \n")
    print(nueva_cadena)
    print('')
    resultado = len(nueva_cadena)
    print("La suma total de éstas es: ", resultado)

vocales_string()