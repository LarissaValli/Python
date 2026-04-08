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

if idade <= 9:
    print('Mirim')
elif idade < 9 and idade >= 14:
    print('Infantil')
elif idade <= 14 and idade >= 19:
    print('Junior')
elif idade <= 19 and idade >= 20:
    print('Sênior')
else:
    print('Master')

#Exercício 7

peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))

imc = peso / (altura **2)

if imc < 18.5:
    print('Abaixo do peso!')
elif imc < 18.5 and imc >= 25:
    print('Peso ideal!')
elif imc < 25 and imc >= 30:
    print('Sobrepeso!')
elif imc < 30 and imc >= 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')

#Exercício 8

produto = float(input('Qual o preço do produto? R$:'))

dinheiroCheque = produto - (produto * 10 / 100)
dinheiro = produto - (produto * 5 / 100)
cartao2x = produto
cartao3x = produto + (produto * 20 / 100)

if produto == dinheiroCheque:
    print(f'O valor do produto é R$: {produto} com o desconto de 10% para pagamento à vista no cheque ou cartão, fica R$: {dinheiroCheque} ')
elif produto ==dinheiro:
    print(f'O valor do produto é R$: {produto} com o desconto de 5% para pagamento à vista em dinheiro, fica R$: {dinheiro} ')
elif produto == cartao2x:
    print(f'O produto tem preço normal')
elif produto == cartao3x:
    print(f'O valor do produto é R$: {produto} com o acréscimo de 20% para pagamento em 3x no cartão, fica R$: {cartao3x} ')

#Exercício 9












