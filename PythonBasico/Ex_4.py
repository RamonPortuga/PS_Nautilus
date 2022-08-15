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
