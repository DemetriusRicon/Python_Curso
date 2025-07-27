'''
Uma Generator Expression em Python é uma forma concisa de criar um gerador, que é um objeto que produz valores sob demanda (lazy evaluation),
em vez de armazenar todos os valores na memória de uma vez. Ela se parece com uma list comprehension, mas usa parênteses em vez de colchetes.
'''

from sys import getsizeof

lista = [x * 10 for x in range(10000)]
print(lista)
print(f' O tamanho da sua lista em bytes = {getsizeof(lista)}')


print('\n')
print('\n')


numeros = (x * 10 for x in range(100000))
print(numeros)
print(f' O tamanho da sua lista em bytes = {getsizeof(numeros)}')

'''
**Resumo:**  
Generator Expressions são úteis para trabalhar com grandes volumes de dados ou fluxos infinitos,
 pois só produzem um item por vez, tornando o código mais eficiente em termos de memória.'''