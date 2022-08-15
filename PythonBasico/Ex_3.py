#3- Diga se um número qualquer é um palíndromo
def checa_palindromo(n):
    if n == n[::-1]:
        print("O número digitado é um palíndromo")
    else:
        print("O número digitado não é um palíndromo")

n = input("Entre com o número desejado:\t")
checa_palindromo(n)
