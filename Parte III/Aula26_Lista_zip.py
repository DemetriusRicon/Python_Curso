# list() é uma função built-in (interna) do Python usada para criar objetos do tipo lista (list). 

marca = ['GM', 'HONDA', 'Mitsubishi', 'FIAT']
modelo = ['ONIX','CIVIC', 'LANCER', 'UNO']

veiculo = zip(marca, modelo)

print(list(veiculo))



#Evite usar list() em objetos que não são iteráveis (ex: int, float), pois isso gerará um erro:

# Um iterável é um objeto que pode ser percorrido item por item (por exemplo, em um for). Exemplos comuns de iteráveis são:
# strings ("abc")
# listas ([1, 2, 3])
# tuplas ((1, 2))
# sets ({1, 2})
# dicionários (ao iterar, retorna as chaves)
# objetos que implementam o método especial __iter__()


#https://www.w3schools.com/python/python_lists.asp