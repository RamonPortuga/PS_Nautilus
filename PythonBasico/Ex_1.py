"""
1- Faça um programa que diga se o primeiro e o último ítens de uma
lista são iguais(deve funcionar para qualquer lista, ou seja, a
quantidade de ítens não é fixa)
"""

import numpy as np

def checa_lista(lista):
    if(lista[0] == lista[len(lista) - 1]):
        print("O primeiro item e o último são iguais")
    else:
        print("O primeiro item e o último são diferentes")

lista = [np.float64(x) for x in input("Entre com a lista = ").split(',')]
checa_lista(lista)
