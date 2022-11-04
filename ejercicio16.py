"""
Ubbi Dubbi es un "lenguaje" de broma utilizado como lenguaje secreto en niños de países de habla inglesa.
Su regla es simple.
Se deben anteponer ub a todas las vocales en una palabra. Ejemplo: mi milk se convierte en mubilk,
python se convierte en pythubon y example se convierte en ubexubamplube (En palabras largas puede ser difícil de pronunciar).
Con esto en mente, define una función que permita realizar la traducción del ingles al Ubbi Dubbi.
La función debe cumplir con los siguiente requerimientos.
La función debe tener por nombre ubbi_dubbi.
La función debe recibir como valor de entrada el string que se desea convertir
(Se asume que se encuentra en ingles).
La función debe retornar la traducción de cada palabra al Ubbi Dubbi.
"""

def ubbi_dubbi():
    
    word = input("Enter a word to translate to Ubi Dubbi: ")
    
    letters = []
    
    for i in word:
        if i in 'aeiou':
            letters.append('ub')
        letters.append(i)
    
    return ''.join(letters)

print(ubbi_dubbi())