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