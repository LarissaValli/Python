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

from time import sleep
for c in range(10, -1, -1):
    print(f'Contagem regressiva: {c}')
    sleep(1)
print('Feliz ano novo!')

#Exercício 2

for c in range(1, 51, 2):
    print(c, end=' ')
print('Fim')

#Exercício 3

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os números ímpares {cont} múltiplos de 3, entre 1 e 500 é {soma}!')

#Exercício 4

n = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c}')
print('Fim')

#Exercício 5

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite um valor: {c}'))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} números pares e a soma entre eles foi {soma}!')

#Exercício 6

primeiro =int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print(f'{c}', end=' > ')
print('Fim')

#Exercício 7

n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m]', end=' ')
        tot += 1
    else:
        print('\033[31m]', end=' ')
    print(f'{c}', end=' ')
print(f'O número {n} foi divisível {tot} vezes!')

#Exercício 8

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

#Exercício 9
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess} pessoa nasceu?'))
    idade = atual - nasc
    print(f'Essa pessoa tem {idade} anos!')
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade!')
print(f'E também tivemos {totmenor} pessoas menores de idade!')

# Aula 14 - Exercício 1

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')

#Exercício 2

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Escolha a opção desejada:
    [1] Somar
    [2] Multiplicar
    [3] Maior)
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {soma}!')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é igual a {produto}!')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}!')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')

#Exercício 3

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'{f}')

#Exercício YouTube

n = 0
while n <= 10:
    print(f'O número é {n}')
    n += 1
#-----------------------------------
n = int(input('Digite um número para fazer a tabuada: '))
for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c}')
print('Fim')
#------------------------------------
palavra = str(input('Digite uma palavra ou frase: '))
v = 0
vogais = 'AEIOUaeiou'
for letras in palavra:
    if letras in vogais:
        v += 1
print(f'A palavra {palavra} tem {v} vogais!')
#------------------------------------
#Escreva a tabuada de 1 a 100







    

































