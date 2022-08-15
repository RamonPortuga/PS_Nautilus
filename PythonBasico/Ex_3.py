#3- Diga se um número qualquer é um palíndromo
def checa_palindromo(n):
    if n == n[::-1]:
        print("O número digitado é um palíndromo")
    else:
        print("O número digitado não é um palíndromo")

n = input("Entre com o número desejado:\t")
checa_palindromo(n)

"""
EXPLICAÇÃO:
Nesse programa, bastou-se criar uma função checa_palindromo e, dentro
dela, fazer uso de manipulação de strings para checar o número dado.
Uma breve observação é que a entrada não foi lida como um número int
ou float, para facilitar a manipulação.

Exemplos:
    Entrada: 999
    Saída: O número digitado é um palíndromo

    Entrada: 10
    Saída: O número digitado não é um palíndromo

    Entrada: 9
    Saída: O número digitado é um palíndromo

    Entrada: 858
    Saída: O número digitado é um palíndromo

    Entrada: 716
    Saída: O número digitado não é um palíndromo
"""
