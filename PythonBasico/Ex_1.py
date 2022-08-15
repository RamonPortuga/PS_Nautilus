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

"""
EXPLICAÇÃO:
O funcionamento desse programa é bem simples, o programa lê a lista
usando list comprehension e passa por parâmetro a lista lida para a
função checa_lista(lista) e compara o primeiro elemento da lista com
o último.

Exemplos:
    Entrada: 1,2,3,4,5,6,7,1
    Saída: O primeiro item e o último são iguais

    Entrada: 1,2,1,3,4,5
    Saída: O primeiro item e o último são diferentes

    Entrada: 1, 1.0
    Saída: O primeiro item e o último são iguais
"""
