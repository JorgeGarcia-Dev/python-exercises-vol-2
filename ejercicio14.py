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

user_word = input("Enter a word to translate to Pig Latin: ")

first_letter = user_word[0]

def pig_latin():
    
    if first_letter in 'aeoiu':
        pig_latin = user_word + way
        print("The word in Pig Latin is: ", pig_latin)
    else:
        length_word = len(user_word)
        remove_first_letter = user_word[1:length_word]
        pig_latin = remove_first_letter + first_letter + ay
        print("The word in Pig Latin is: ", pig_latin)

pig_latin()