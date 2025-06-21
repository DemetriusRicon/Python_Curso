'''
 O que é um set?

Um **set** (conjunto) em Python é uma coleção não ordenada de elementos únicos, ou seja, não permite itens duplicados.

Pontos importante

**Elimina duplicatas:** Ao converter uma lista para set, os elementos repetidos são removidos automaticamente.
**Não ordenado:** A ordem dos elementos podem mudar e não é garantida.
**Operações matemáticas:** Sets permitem operações como união, interseção e diferença.

'''

### Exemplo de operações

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1 | set2)  # União: {1, 2, 3, 4}
print(set1 & set2)  # Interseção: {2, 3}
print(set1 - set2)  # Diferença: {1}



#Uso sets quando preciso garantir que não haja elementos duplicados em uma coleção de dados.

# Lista 1 com itens duplicados
lista1 = [1, 2, 2, 3, 4, 4, 4, 5]

# Lista 2 com itens duplicados
lista2 = ['a', 'b', 'b', 'c', 'd', 'd', 'e']


num1 = set(lista1)
var2 = set(lista2)

print(num1)
print(var2)


#----------
lista3 = [1,2,32,4,5]

variavel_set = set(lista3)

print(variavel_set)
#Remove um elemento do set, falha se nao houver.
variavel_set.remove(32)
#Add só pega um elemento de cada vez ?
variavel_set.add(91)

lista_insercao_set =[88,99,11,00,12,21,64,21,64]

for i in lista_insercao_set:
    variavel_set.add(i)

print(variavel_set)


#------
frutas = ['maca', 'banana', 'manga' ,'laranja']

frutas_set = set(frutas)
frutas_set.add('uva')
print(f' Adicionamos a fruta anterior, sua lista agora contem : {frutas_set}')
frutas_set.remove('banana')
print(f' Removemos a fruta anterior, sua lista agora contem : {frutas_set}')
frutas_set.discard('manga')
print(f' Descartamos a fruta anterior, sua lista agora contem : {frutas_set}') 