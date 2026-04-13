#        Condicionais aninhadas

nome = str(input('Qual seu nome?'))
if nome == 'Larissa':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Clara, Laura, Luiza, Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
    print(f'Tenha um bom dia, {nome}!')

#------------------------------------
#         Estrutura de repetição for

for c in range(0, 7, 2):
    print(c)
print('Fim')

n = int(input('Digite um número: '))
for c in range (0, n+1):
    print(c)
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: ')) 
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('Fim')

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores é {s}!')

#          Repetição While

'''for c in range(1, 10):
    print(c)
print('Fim')'''

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')
#-------------------------------------
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')
#-------------------------------------
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
#-------------------------------------
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper() 
print('Fim')
#-------------------------------------
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')



