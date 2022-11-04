"""
Desarrolla un programa que permita crear una lista de longitud N de números
aleatorios que comprendan del -100 al 100.
"""

print('')
print("Ejercicio crear una lista de números aleatorios entre el -100 y 100: \n")

import random

lista_mix = []

def numeros_aleatorios():
    
    for n in range(10):
        numero = random.randint(-100,100)
        lista_mix.append(numero)

numeros_aleatorios()

print("Lista de números aleatorios positivos y negativos: \n")
for n in lista_mix:
    print(n)

"""
Dada la lista anterior de número aleatorios, desarrolla un programa que permita
conocer la suma de todos los números pares mayores a 0.
"""

print('')
print("Ejercicio sumar todos los números pares mayores a 0: \n")

nueva_lista = []

def suma_pares():
    for n in lista_mix:
        if n > 0 and n % 2 == 0:
                nueva_lista.append(n)

suma_pares()

print('')

print("Los números pares mayores a 0 son: \n")
for n in nueva_lista:
    print(n)
suma = sum(nueva_lista)
print('')
print("La suma de todos los números pares mayores a 0 es: \n")
print(suma)

"""
Dada la lista anterior de número aleatorios, desarrolla un programa que permita
conocer la suma de todos los números pares mayores a 0 y que no se encuentren
entre los rangos 20-29 y 50-59.
"""

print('')
print("Ejercicio sumar todos los números pares mayores a 0 y que se encuentren fuera del rango de 20,29 y 50,59: \n")

nueva_lista_dos = []

def suma_pares_rango():
    for n in lista_mix:
        if (n > 0 and n % 2 == 0) and (n not in range(20, 29) and n not in range(50,59)):
                nueva_lista_dos.append(n)

suma_pares_rango()

print('')

print("Los números pares mayores a 0 y fuera de rango entre 20,29 y 50,59 son: \n")
for n in nueva_lista_dos:
    print(n)
suma = sum(nueva_lista_dos)
print('')
print("La suma de todos los números pares mayores a 0 y fuera de rango entre 20,29 y 50,59 es: \n")
print(suma)

"""
Dada la lista anterior de números aleatorios, desarrolla un programa en que imprima en consola todos los números negativos.
"""

print('')
print("Ejercicio imprimir todos los números negativos: \n")

print('')

def numeros_negativos():
    
    print('Los números negativos son: \n')
    for n in lista_mix:
        if n < 0:
            print(n)

numeros_negativos()

print('')

"""
Dada la lista anterior de números aleatorios, desarrolla un programa en que imprima en consola el número mayor y el número menor.
"""

print('')
print("Ejercicio número mayor y número menor: \n")

for n in lista_mix:
    mayor = max(lista_mix)

print("El número mayor es: ", mayor)

print('')

for n in lista_mix:
    menor = min(lista_mix)

print("El número menor es: ", menor)

"""
Dada la lista anterios de números aleatorios, desarrolla un programa en que imprima en consola
el segundo número mayor y el tercer número menor.
"""

print('')
print("Ejercicio segundo y tercer número mayor: \n")

lista_mix.sort()
print("El segundo número mayor es: ", lista_mix[-2])
print("El tercer número mayor es: ", lista_mix[-3])