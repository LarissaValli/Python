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

resultado = n1 + n2 / 2

print(f'Sua nota média de {n1} + {n2} / 2 
\n é de {resultado}')

#exercício 4

metros = int(input('Digite o metro: '))

centimetros = metros * 100
milimetros =  metros * 1000

print(f'O valor do {metros} em centimetros é de {centimetros} e em milimetros {milimetros}')

#exercício 5










