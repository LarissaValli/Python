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





