# Exercícios de Python Básico - PS Nautilus

Esse arquivo foi criado no intuito concentrar em um único arquivo, as explicações dos programas utilizando Python Básico
(Obs: Todos os códigos foram comentados e as explicações aqui presentes foram retiradas deles)

### 1- Faça um programa que diga se o primeiro e o último ítens de uma lista são iguais(deve funcionar para qualquer lista, ou seja, a quantidade de ítens não é fixa)

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



### 2- Faça um programa que diga o maior divisor primo de um número dado como input

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



### 3- Diga se um número qualquer é um palíndromo

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



### 4- Dê a soma de todos os números primos menores que 1000

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