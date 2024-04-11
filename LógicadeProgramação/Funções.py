#1 - Faça um programa para imprimir:
#1
#2 2
#3 3 3
#.....
#n n n n n n ... n
#para um  informado pelo usuário. Use uma função que receba um valor  inteiro e imprima até a n-ésima linha.

def programa_imprimir(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=' ')
        print()

n = int(input("Digite um valor inteiro para n: "))

programa_imprimir(n)


#2 Escreva uma função chamada fatorial que calcula o fatorial de um número inteiro fornecido como argumento

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

numero = int(input("Digite um número inteiro para calcular o fatorial: "))
resultado_fatorial = fatorial(numero)
print(f'O fatorial de {numero} é: {resultado_fatorial}')


# 3 - Escreva uma função chamada verifica_primo que verifica se um número é primo ou não e retorna True ou False.

def verifica_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número para verificar se é primo: "))
resultado = verifica_primo(numero)

if resultado:
    print(f'{numero} é um número primo.')
else:
    print(f'{numero} não é um número primo.')

# 4 - Escreva uma função chamada inverte_string que aceita uma string como parâmetro e retorna a string invertida.

def inverte_string(s):
    return s[::-1]


entrada = input("Digite uma string para inverter: ")
resultado = inverte_string(entrada)

print(f'A string invertida é: {resultado}')


#5 - Escreva uma função chamada maior_valor que aceita uma lista de números como parâmetro e retorna o maior valor na lista.

def maior_valor(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    return max(lista)


numeros = [10, 5, 8, 15, 3]
maior = maior_valor(numeros)

print(f'O maior valor na lista é: {maior}')

# 6 - Escreva uma função chamada conta_vogais que aceita uma string como parâmetro e retorna o número de vogais na string.

def conta_vogais(s):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador


texto = input("Digite uma string para contar as vogais: ")
num_vogais = conta_vogais(texto)

print(f'O número de vogais na string é: {num_vogais}')

# 7 - Escreva uma função chamada soma_quadrados que aceita uma lista de números como parâmetro e retorna a soma dos quadrados desses números
def soma_quadrados(numeros):
    soma = 0
    for numero in numeros:
        soma += numero ** 2
    return soma


lista_numeros = [1, 2, 3, 4, 5]
resultado = soma_quadrados(lista_numeros)

print(f'A soma dos quadrados dos números é: {resultado}')

# 8 - Escreva uma função chamada imprime_tabuada que aceita um número inteiro como parâmetro e imprime a tabuada desse número de 1 a 10.

def imprime_tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')


numero = int(input("Digite um número inteiro para imprimir a tabuada: "))
imprime_tabuada(numero)



