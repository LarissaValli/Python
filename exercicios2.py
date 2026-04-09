#Aula 12- Exercício 1

casa = float(input('Qual o valor da casa? R$: '))
salario = float(input('Informe o valor do salário do comprador R$: '))
anos = int(input('Quantos anos de financiamento?'))

prestacao = casa / (anos * 12)

if prestacao > salario * 0.3:
    print('Empréstimo negado!')
elif prestacao <= salario * 0.3:
    print('Empréstimo aprovado')
else:
    print('Valor inválido!')

#Exercício 2

n = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[1] binário
[2] octal
[3]hexadecimal''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print(f'{n} convertido para binário é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convertido para octal é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção inválida! Tente novamente!')

#Exercício 3

n1 = int(input('Digite um número:'))
n2 = int(input('Digite o segundo número:'))

if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
else:
    print('Não existe número maior, os dois são iguais!')

#Exercício 4

from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano de nascimento, para saber se deve ou não se alistar: '))

idade = atual - nasc

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento!')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}!')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos!')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}!')


#Exercício 5

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

media = (n1 + n2) / 2

print(f'A média entre {n1:.1f} e {n2:.1f}, é {media:.1f}')

if media < 5.0:
    print('Aluno reprovado!')
elif media >= 5.0 and media <= 6.9:
    print('Aluno em recuperação!')
elif media >= 7.0:
    print('Aluno aprovado!')

#Exercício 6

ano = int(input('Digite o ano de nascimento:'))

idade = 2026 - ano
print(f'O atleta tem {idade} anos!')

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')


#Exercício 7

peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))

imc = peso / (altura **2)

if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')

#Exercício 8

produto = float(input('Qual o preço do produto? R$:'))
preço = float(input('Preço das compras R$: '))
print('''Escolha a forma de pagamento:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual é a sua opção? '))

if opcao == 1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 5 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
elif opcao == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS!')
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    parcela = total / 3
    print(f'Sua compra será parcelada em 3x de R${parcela:.2f} COM JUROS!')

#Exercício 9

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0: #Pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Opção inválida!')

elif computador == 1: #Papel
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Opção inválida!')

elif computador == 2: #Tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Opção inválida!')

#Aula 13 - Exercício 1
#


























