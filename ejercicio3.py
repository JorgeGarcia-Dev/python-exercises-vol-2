"""
Desarrolla una programa que permita conocer si todos los elementos
de una lista son el resultado de la suma del elemento anterior más 10.
"""

lista_1 = [1,11,21,31,41,51]
lista_2 = [1,11,23,31,41,51]

def mas_10():

    if lista_1[0] + 10 == lista_1[1] and lista_1[1] + 10 == lista_1[2] and lista_1[2] + 10 == lista_1[3] and lista_1[3] + 10 == lista_1[4] and lista_1[4] + 10 == lista_1[5]:
    # if lista_2[0] + 10 == lista_2[1] and lista_2[1] + 10 == lista_2[2] and lista_2[2] + 10 == lista_2[3] and lista_2[3] + 10 == lista_2[4] and lista_2[4] + 10 == lista_2[5]:
        print(True)
    else:
        print(False)

mas_10()
