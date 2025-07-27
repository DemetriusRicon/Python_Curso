#O filter em Python é uma função embutida que permite filtrar elementos de um iterável (como listas, tuplas, etc.)
#  com base em uma função que retorna True ou False para cada elemento.

valores = [2,4,6,8,10,12,14,16,18,20]


def funcao_remove10(x):
    return x>10

print(list(filter(funcao_remove10,valores)))