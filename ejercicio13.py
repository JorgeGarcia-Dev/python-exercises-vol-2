"""
Define una función que permita conocer si un String tiene un formato de IP v4.
Para este ejercicio es necesario validar que existan 4 puntos dentro del string.
"""

ip_address = input("Ingresa una dirección IP: ")
puntos_totales = []

for n in ip_address:
    if n == '.':
        puntos_totales.append(n)

resultado = len(puntos_totales)

if resultado >= 4:
    print("Este Sting tiene un formato IPv4.")