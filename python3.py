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
