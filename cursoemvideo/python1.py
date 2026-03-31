
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







