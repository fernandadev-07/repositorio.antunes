# 1. Faça um programa que possua um Dicionário, adicione elementos ao dicionário e os mostre na tela.

estoque_mercado = {}

estoque_mercado[1] = 'Leite'
estoque_mercado[2] = 'Café'
estoque_mercado[3] = 'Feijão'

print("Itens do mercado: ", estoque_mercado)

# 2. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.

mercado = {}

for i in range(3):
  produto = str(input('digite o nome do produto: '))
  preco = float(input('digite o valor no produto '))
  mercado[produto] = preco

for produto, preco in mercado.items():
    print(f"produto = {produto} - valor = {preco}")

# 3. Faça um programa, utilizando Dicionários, que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas.

escola = []

for i in range(4):
    nota = float(input(f'Digite a nota do aluno: '))
    escola.append(nota)

media = sum(escola) / len(escola)

print(f"Notas dos alunos: {escola}")
print(f"Média da pessoa: {media}")

# 4. Faça um programa, utilizando Dicionários, que:
#1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .
#2° Passo: Peça para o usuário inserir um número.
#3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.

caixa_misteriosa = {}

for i in range(4):
    coisa = input('Digite algo misterioso (uuuh): ')
    caixa_misteriosa[i + 1] = coisa

numero_escolhido = int(input('Digite um número para descobrir o que está na Caixa Misteriosa: '))

if numero_escolhido in caixa_misteriosa:
    coisa_descoberta = caixa_misteriosa[numero_escolhido]
    print('O mistério dentro da Caixa Misteriosa na posição que você escolheu é:', coisa_descoberta)
else:
    print('Número inválido. Tente novamente.')

#5. Faça um programa, utilizando Dicionários, que:
#1° Passo: Peça para o usuário inserir o nome de três funcionários e os mostre na tela.
#2° Passo: Peça para o usuário demitir um funcionário e mostre na tela os funcionários restantes.

empresa = {}

for i in range(3):
    funcionario = input('Digite o nome do funcionário: ')
    empresa[i + 1] = funcionario

opcao = int(input('Digite o número do funcionário a ser excluído: '))

if opcao in empresa:
    del empresa[opcao]
    print(f'Funcionário {opcao} excluído com sucesso!')
else:
    print('Número de funcionário inválido. Tente novamente.')

print('Lista de funcionários:', empresa)


