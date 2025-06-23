# https://docs.python.org/3/library/functions.html#map
# A função map() em Python aplica uma função a cada item de um iterável (como uma lista ou tupla) e retorna um iterador com os resultados.
# Ela é útil para transformar coleções de dados de forma eficiente,sem a necessidade de escrever loops explícitos.

lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(lista_teste)


def calcular_dados(argumento):
    usar_lambda = lambda argumento : argumento ** 2
    return usar_lambda(argumento)

lista_resultado = map(calcular_dados,lista_teste)

print(f'Resultado antes da conversao : {type(lista_resultado)}\n' )

print(f'Resultado pos conversao : {list(lista_resultado)}')




# Tornando mais elegante. 
print(f' O Resultado da lista  = {list(map(lambda argumento: argumento**2, lista_teste ))}')
