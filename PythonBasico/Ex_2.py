#2- Faça um programa que diga o maior divisor primo de um número dado como input
def crivo_de_eratostenes(n):
    numeros = [True] * (n + 1)
    
    numeros[0] = False
    numeros[1] = False
    
    primos = []
    
    for numero, primo in enumerate(numeros):
        if primo:
            primos.append(numero)
            
            for i in range(numero * 2, n + 1, numero):
                numeros[i] = False
    return primos

def maior_divisor_primo(n, primos):
    maior = 0
    for i in range (0, len(primos)):
        if(primos[i] <= n):
            if(n % primos[i] == 0):
                maior = primos[i]
        else:
            break
    return maior

n = int(input("Entre com o número desejado:\t"))
primos = []
primos = crivo_de_eratostenes(n)
print("\nO maior divisor primo desse número é:")
print(maior_divisor_primo(n, primos))

"""
EXPLICAÇÃO:
Para esse programa, busquei aumentar a eficiência no processamento
e, para isso, fiz uma função que cria uma lista com os números primos
com base no crivo de eratóstenes. Depois disso, utilizando a função
maior_divisor_primo, ocorre a busca pelo maior divisor primo do número
fornecido pelo usuário.

Exemplos:
    Entrada: 25
    Saída: 5

    Entrada: 100
    Saída: 5

    Entrada: 169
    Saída: 13

    Entrada: 91
    Saída: 13
"""
