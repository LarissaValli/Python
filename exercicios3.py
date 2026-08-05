#Praticando com listas

#1)Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectativas posições na lista.

valores = []

for cont in range(0, 5):
    n = int(input(f'Digite um valor na posição {cont}: '))
    valores.append(n)
print("=-"*30)
print(f'Você digitou os valores {sorted(valores)}')
print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')


#------------------------------------------
#2) Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = [ ]

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
        continuar = str(input('Quer continuar? [S/N] '))
        if continuar in 'Nn':
            print('=-' * 30)
            print('Finalizando...')
            print(f'Você digitou os valores {sorted(valores)}')
            break
    else:
        print('Valor duplicado! Não vou adicionar...')

#------------------------------------------
#3) Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta da inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []

for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n < valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {valores}')

#------------------------------------------
#4)Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A)Quantos números foram digitados. B)A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        continuar = str(input('Quer continuar? [S/N] '))
        if continuar in 'Nn':
            print('=-' * 30)
            print(f'Você digitou {len(valores)} elementos.')
            print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
            if 5 in valores:
                print('O valor 5 está na lista.')
            else:
                print('O valor 5 não está na lista.')
            break
#------------------------------------------
#5) Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

valores = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    if (n % 2 == 0):
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('=-' * 30)
print(f'A lista completa é {sorted(valores)}')
print(f'A lista de pares é {sorted(pares)}')
print(f'A lista de impares é {sorted(impares)}')

#------------------------------------------
#6) Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

#------------------------------------------
#Praticando com listas (parte 2)


#1) Faça um programa que leia nome e pesa de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Os dados foram {princ}')
print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi {mai} Kg. Peso de ', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {men} Kg. Peso de ', end=' ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

#2) Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('=-' * 30)
print(f'Os valores pares digitados foram {sorted(num[0])}')
print(f'Os valores ímpares digitados foram {sorted(num[1])}')

#3) Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
#4) Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')

#5)Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = list()
jogos = list()
print('=-'*30)
print('      JOGA NA MEGA SENA     ')
print('=-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-'*3, f'SORTEANDO {quant} JOGOS', '=-'*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=-'*5, '< BOA SORTE! >', '=-'*5)

#6) Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')


