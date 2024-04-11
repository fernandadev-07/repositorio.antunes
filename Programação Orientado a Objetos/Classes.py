#Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado ** 2

quadrado = Quadrado(5)
print("Lado do quadrado:", quadrado.retornar_lado())
print("Área do quadrado:", quadrado.calcular_area())

quadrado.mudar_lado(7)
print("Novo lado do quadrado:", quadrado.retornar_lado())
print("Nova área do quadrado:", quadrado.calcular_area())

# Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)


if __name__ == "__main__":
    comprimento = float(input("Informe o comprimento do local (em metros): "))
    largura = float(input("Informe a largura do local (em metros): "))

    retangulo = Retangulo(comprimento, largura)

    area_total = retangulo.calcular_area()
    perimetro_total = retangulo.calcular_perimetro()

    area_piso = 1
    comprimento_rodape = 0.1
    quantidade_pisos = area_total / area_piso
    quantidade_rodapes = perimetro_total / comprimento_rodape

    print("\nQuantidade de pisos necessários:", quantidade_pisos)
    print("Quantidade de rodapés necessários:", quantidade_rodapes)

# Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, altura_ganha):
        self.altura += altura_ganha

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} kg, Altura: {self.altura} cm"


pessoa = Pessoa("pedroca", 18, 70, 170)
print("Antes:")
print(pessoa)

pessoa.envelhecer()
pessoa.engordar(2)
pessoa.crescer(1)

print("\nDepois de envelhecer 1 ano, engordar 2 kg e crescer 1 cm:")
print(pessoa)

#   Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque;
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.



class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque de", valor, "realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def __str__(self):
        return f"Número da Conta: {self.numero_conta}, Nome do Correntista: {self.nome_correntista}, Saldo: R${self.saldo:.2f}"

conta1 = ContaCorrente("123456", "ladilson")
print("Antes:")
print(conta1)

conta1.deposito(1000)
print("\nDepois do depósito de R$1000:")
print(conta1)

conta1.saque(500)
print("\nDepois do saque de R$500:")
print(conta1)

conta1.alterar_nome("ladilson silveira")
print("\nDepois de alterar o nome do correntista:")
print(conta1)
