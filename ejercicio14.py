"""
PigLatin es un "lenguaje" de broma utilizado como lenguaje secreto en niños de países de habla inglesa.
Sus reglas son simples.
Si la palabra comienza con una vocal (a, e, i, o, u) se deberá agregar way al final de la palabra. Ejemplos: "air" se convierte en
"airway". "eat" se convierte en "eatway"
Si la palabra comienza con otro carácter, se toma la primera letra y se añade al final, agregando "ay".
Ejemplos: "Python" se convierte en "ythonpay". "Demo" se convierte en "emoday"
Con todo esto en mente, desarrolla una función que permita hacer la traducción entre el Ingles y el Pig Latin.
La función debe cumplir con los siguiente requerimientos. La función debe tener por nombre _pig\latin.
La función debe recibir como valor de entrada el string que se desea convertir (Se asume que se encuentra en inglés).
La función debe retornar la traducción de cada palabra al Pig Latin.
"""

ay = 'ay'
way = 'way'

palabra_usuario = input("Enter a word to translate to Pig Latin: ")

primera_letra = palabra_usuario[0]

def pig_latin():
    
    if primera_letra in 'aeoiu':
        pig_latin = palabra_usuario + way
        print("La palabra en Pig Latin es: ", pig_latin)
    else:
        contador_palabra = len(palabra_usuario)
        remover_primera_letra = palabra_usuario[1:contador_palabra]
        pig_latin = remover_primera_letra + primera_letra + ay
        print("La palabra en Pig Latin es: ", pig_latin)

pig_latin()