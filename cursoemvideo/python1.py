
#---------------------------------------
#           Operadores Aritméticos

#Ordem de precedência
#1 - ()
#2 - **
#3 - * / // %
#4 - + - 

#-----------------------------------------

#           Utilizando módulos

import math 
#from math import sqrt, floor (importando apenas o que irá ser utilizado que é from sqrt e floor.)
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.2f}')

import random
num = random.randint(1, 10)
print(num)

#------------------------------------------
#             Manipulando texto

frase = 'Curso em video Python'
print(frase.count('o'))

#------------------------------------------
#             Condições

nome = str(input('Qual seu nome? '))

if nome == 'Larissa':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}')

n1 = str(input('Digite a primeira nota:'))
n2 = str(input('Digite a segunda nota:'))

media = (n1 + n2) / 2

print(f'A sua média foi {media:1f}')
if media >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')







