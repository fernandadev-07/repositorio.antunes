#01 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor1 = float(input(' digite um valor: '))

if valor1 > 0:
  print(' este valor é postivo')

elif valor1 < 0:
  print(' este valor é negativo')

else:
    print('este valor é zero')


#02 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str
sexo = str(input(' digite se você é feminino(f) ou masculino(m)'))

if sexo == 'f':
  print ('você é feminino')
elif sexo == 'm':
  print ('você é masculino')
else:
  ('você é inválido(a)')


#03 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str
letra = str(input('digite uma letra: '))

if letra in 'aeiou':
  print ('sua letra é uma vogal')
else:
  print ('sua letra é consoante')

#4 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float
nota2 = float
media = float

nota1 = float(input('digite a primeira nota '))
nota2 = float(input('digite a segunda nota '))
media = float

media= (nota1 + nota2) /2

if media == 10:
  print("voce foi aprovado com distinção! ")
elif media < 7:
  print("voce foi reprovada! ")
elif media > 7:
  print("voce foi aprovado! ")


# 5 - Faça um Programa que leia três números e mostre o maior deles.

num1 = float
num2 = float
num3 = float

num1 = float(input("digite o primeiro numero:  "))
num2 = float(input("digite o segundo numero:  "))
num3 = float(input("digite o terceiro numero: "))

if (num1 > num2) and (num1 > num3):
  print("o numero 1 é maior")
elif(num2>num1) and (num2>num3):
  print("o numero 2 é maior")
else:
  print("o numero 3 é maior ")


# 6 - Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float
num2 = float
num3 = float

num1 = float(input("digite o primeiro numero "))
num2 = float(input("digite o segundo numero "))
num3 = float(input("digite o terceiro numero "))

if (num1<num2) and (num1 < num3):
  print("o numero 1 é menor ")
elif(num2<num1) and (num2<num3):
  print("o numero 2 é menor ")
else:
  print("o numero 3 é menor ")

# 7 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco_produto1 = float(input("Digite o preço do primeiro produto: "))
preco_produto2 = float(input("Digite o preço do segundo produto: "))
preco_produto3 = float(input("Digite o preço do terceiro produto: "))


if preco_produto1 < preco_produto2 and preco_produto1 < preco_produto3:
    produto_mais_barato = "Produto 1"
elif preco_produto2 < preco_produto1 and preco_produto2 < preco_produto3:
    produto_mais_barato = "Produto 2"
else:
    produto_mais_barato = "Produto 3"

print(f"Você deve comprar o {produto_mais_barato}, pois é o mais barato.")

# 8 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float
num2 = float
num3 = float

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Cria uma lista com os números
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Exibe os números em ordem decrescente
print("Números em ordem decrescente:", numeros)
