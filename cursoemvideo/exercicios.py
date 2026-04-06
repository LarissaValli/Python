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

#Aula 9 -  Exercício 1

nome = str(input('Digite seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(nome.find(' '))

#Exercício 2

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar {m}')

#Exercício 3

cidade = str(input('Digite o nome da sua cidade aqui: ')).strip()
print(cidade[:5].upper() == 'Santo')

#Exercício 4



#Exercício 5

frase = str(input('Digite uma frase:')).upper().strip()
print(f'A letra A aparece {frase.count('A')}vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find('A')+1}')
print(f'A última letra A pareceu na posição{frase.rfind('A')+1}')


#Exercício 6

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')

# Aula 10 - Exercício 1

from random import randint
from time import sleep
computador = randint(0, 5) #Faz o pc pensar
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))#Jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabêns, você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}')

#Exercício 2

velocidadeCar = float(input('Digite aqui a velocidade do carro: '))

multa = (velocidadeCar - 80) * 7

if (velocidadeCar > 80):
    print(f'Você foi multado! A multa vai custar R$ 7,00 por cada Km acima do limite. Então sua multa é de {multa}')

#Exercício 3

n = int(input('Digite um número: '))
resultado = n % 2

if resultado == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é impar.')

#Exercício 4

viagem = float(input('Qual a distância de uma viagem em KM? '))

curta = viagem * 0.50
longa = viagem * 0.45

if(viagem <= 200):
    print(f'Se a viagem for de até 200km, será cobrado 0,50 por km. O valor a ser pago em sua viagem é de {curta}')
else:
    print(f'Viagem longa, terá um custo de {longa:.2f}')

#Exercício 5

ano = int(input('Que ano quer analisar: '))
if ano % 4 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')


#Exercício 6

s = float(input('Qual seu salário: '))

if (s <= 1.250):
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print(f'Quem ganhava R${s:.2f} passa a ganhar R${novo:.2f}.')




















