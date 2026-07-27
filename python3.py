#Listas em Python

lanche = ["hamburguer", "suco", "pizza", "pudim"]
lanche[3] = "bolo" #Alterando o valor do índice 3
print(lanche) #Imprimindo a lista atualizada

#-------------------------------------------------------
lanche.append("cookie") #Adicionando um elemento no final da lista
print(lanche) #Imprimindo a lista atualizada

lanche.insert(0, "coca-cola") #Adicionando um elemento no índice 0
print(lanche) #Imprimindo a lista atualizada

#Para apagar um elemento da lista.
del lanche[3] #Removendo o elemento do índice 3
print(lanche) #Imprimindo a lista atualizada

#Para apagar o último elemento da lista. Mas se passarmos um índice como parâmetro, ele apagará o elemento do índice informado.
lanche.pop(3) #Removendo o elemento do índice 3
print(lanche) #Imprimindo a lista atualizada

#Para remover um elemento da lista pelo valor, podemos usar o método remove(). Ele remove a primeira ocorrência do valor informado.
lanche.remove("suco") #Removendo o elemento "suco" da lista
print(lanche) #Imprimindo a lista atualizada

#Para saber se um elemento está na lista e se estiver, ele irá ser removido. Caso contrário, ele não fará nada.
if "pizza" in lanche:
    lanche.remove("pizza") #Removendo o elemento "pizza" da lista   

valores = list(range(4, 11)) #Criando uma lista com os valores de 4 a 10

valores = [8, 2, 5, 4, 9, 3, 0] #Criando uma lista com valores aleatórios
valores.sort() #Ordenando a lista em ordem crescente
valores.sort(reverse=True) #Ordenando a lista em ordem decrescente
len(valores) #Retorna o tamanho da lista

#-----------------------------------------

#Exercício com professor

num = [2, 5, 9 , 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a[:] #Copia a lista A para a lista B
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

#------------------------------------------
#Listas (Parte 2)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0]) #Imprime o nome João
print(galera[2][1]) #Imprime a idade 13

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

