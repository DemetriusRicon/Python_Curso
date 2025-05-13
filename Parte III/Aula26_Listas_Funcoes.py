#Existem varias funções de uma lista disponveis na estrutura do Python. 


numeros =[1,2,3,4,5,6,7,8,9,411,12,14,45,78,75,78,75,345789]

#Adiciona um valor ao final da lista
numeros.append(9999)

print(numeros[-1])

# A remoção de um item da lista se da pelo seu valor + endereço.
# Mesmo duplicando uma ocorrencia o mesmo nao será removido de uma unica vez. 
numeros.remove(78)

print(numeros)

# Insere um valor numa posicao especifica
numeros.insert(4,1001)
print(numeros)

# Remove de uma posicao especifica
numeros.pop(0)
print(numeros)

# Remove de uma posicao especifica
numeros.pop(0)
print(numeros)

