#4- Dê a soma de todos os números primos menores que 1000

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

def soma_dos_primos(primos):
    soma = 0
    for i in range (0, len(primos)):
        soma += primos[i]
    return soma

n = 1000
primos = []
primos = crivo_de_eratostenes(n)
print("Realizando o somatório usando a função soma_dos_primos:")
print(soma_dos_primos(primos))
print("\nFazendo a prova real usando a função sum(lista):")
print(sum(primos))

"""
EXPLICAÇÃO:
Para esse programa, busquei aumentar a eficiência no processamento
e, para isso, fiz uma função que cria uma lista com os números primos
com base no crivo de eratóstenes. Depois disso, utilizando a função
soma_dos_primos, ocorre o somatório dos números primos. Como forma
de confirmar o resultado, ocorre uma checagem do valor apresentado
usando a função sum(lista). 

Exemplo:
    Saída:
    
    Realizando o somatório usando a função soma_dos_primos:
    76127

    Fazendo a prova real usando a função sum(lista):
    76127
"""
