nome = input('Qual seu nome?')
idade = input('Quantos anos você tem?')
peso = input('Qual seu peso')

print(nome, idade, peso)

#--------------------------
#         Tipos primitivos

n = float(input('Digite um número: '))

print(n)

n = input('Digite algo: ')
print(n.isnumeric())
#obs: Vai dizer se é possível converter o valor em um número com o tipo primitivo int antes dele.

n = input('Digite algo: ')
print(n.isalpha())
# Se ele é letra.

n = input('Digite algo: ')
print(n.isalnum())
# Se o valor tem número e letra. Ex: 3a (é alpha numerico)

n = input('Digite algo: ')
print(n.isupper())
#Vai analisar se está somente com letras maiusculas.

#---------------------------------------
#           Operadores Aritméticos





