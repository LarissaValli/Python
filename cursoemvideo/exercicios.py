#atividade 1

nome = input('Qual seu nome?')
print('Boas vindas', nome, 'prazer em conhecer você!')

#---------------------------

dia = input('Qual dia você nasceu?')
mes = input('Qual mês?')
ano = input('E qual ano você nasceu?')

print('Você nasceu:', dia, mes, ano)

#---------------------------

n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite outro número:'))

soma = n1 + n2

print(f'A soma de {n1} + {n2} é: {soma}')

#----------------------------

#aula 5 - lista de exercicio.

#exercício 1

print('Olá, mundo!')

#exercício 2

nome = input('Qual seu nome?')
print(f'É um prazer conhecer você,{nome}!')

#aula 6 - Exercício 01

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2
print(f'A soma de {n1} e {n2} é: {soma}')

#Exercício 2

x = input('Digite algo: ')

n = x.isnumeric()
l = x.isalpha()
a = x.isalnum()
m = x.isupper()

print(f'{x} É número? {n}')
print(f'{x} É letra? {l}')
print(f'{x} É alphanumerico? {a}')
print(f'{x} É letra maiuscula? {m}')

#Exercício - Operadores Aritméticos

#exercício 1

n = int(input('Digite um número: '))
antecessor = n - 1
sucessor = n + 1

print(f'O número é {n}, seu antecessor é {antecessor} e seu sucessor {sucessor}')

#exercício 2

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raizQuadrada = n ** (1/2)

print(f'O dobro do número {n} é {dobro} o triplo {triplo} e a raiz quadrada é {raizQuadrada}')

#exercício 3 

n1 = float(input('Digite sua nota aqui:'))
n2 = float(input('Digite a segunda nota: '))

resultado = (n1 + n2) / 2

print(f'Sua nota média de {n1} + {n2} / 2 é de {resultado}')

#exercício 4

metros = float(input('Digite o metro: '))

centimetros = metros * 100
milimetros =  metros * 1000

print(f'O valor do {metros} em centimetros é de {centimetros} e em milimetros {milimetros}')

#exercício 5

num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)

print(f'{num} x {1} = {num*1}')
print(f'{num} x {2} = {num*2}')
print(f'{num} x {3} = {num*3}')
print(f'{num} x {4} = {num*4}')
print(f'{num} x {5} = {num*5}')
print(f'{num} x {6} = {num*6}')
print(f'{num} x {7} = {num*7}')
print(f'{num} x {8} = {num*8}')
print(f'{num} x {9} = {num*9}') 
print(f'{num} x {10} = {num*10}')

print('-' * 12)

#Exercício 6

carteira = float(input('Quanto que você tem na carteira? R$'))
#dolar hoje - 5,23
dol = (carteira / 5.23)

print(f'Você tem na carteira R${carteira:.2f}, dá para comprar US${dol:.2f} doláres.')

#Exercício 7

larg = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))

area = larg * alt
print(f'Sua parede tem a dimensão de {larg} x {alt} e sua área é de {area}m2.')

tinta = area / 2

print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')

#Exercício 8

preco = float(input('O preço do produto é: R$ '))
novoPreco = (preco * 5 / 100)

print(f'O preço do produto era de R${preco}, com o desconto de 5% ficou R${novoPreco}.')

#Exercício 9

salario = float(input('Qual o salário do funcionário R$: '))
novoSalario = salario + (salario * 15 / 100)

print(f'O funcionário receberá um novo salário de 15% de aumento. Salário anterior de R${salario:.2f} foi para R${novoSalario:.2f}.')

#Exercício 10

celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = ((9 * celsius / 5) + 32)
print(f'A temperatura de {celsius}°C corresponde a {fahrenheit}°F!' )

#Exercício 11

km = float(input('Quantidade percorrido de Km'))
dias = int(input('Quantos dias o carro foi alugado: '))

pagar = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${pagar:.2f}')

#Aula 8 - Exercício 1

import math
numReal = float(input('Digite um número: '))
num = math.trunc(numReal)
print(f'O número {numReal} tem a parte inteira {num}')

#Exercício 2

import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)

print(f'Entre seus 4 alunos, o que foi sorteado a apagar o quadro é {escolhido}.')

#Exercício 3

import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('A ordem de apresentação será')
print(lista)

#Exercício 4

#import pygame

















