# O Demetrius é um excelente [programador]. 

nome = 'Demetrius'
sobrenome = 'Ricon'
profissao = 'Analista'

texto = 'O ' + nome + '' + sobrenome + ' e um excelente' + '[ ' + profissao + ' ]'

print (texto)

#Usando formated Strings no sistema
texto2 = f'O {nome} {sobrenome} e um excelente [{profissao}]'

print (texto2)


#Usando métodos de Strings
mensagem = 'Eu adoro comida caseira de Minas Gerais'

print(mensagem.lower())
print(mensagem.upper())
print(mensagem.capitalize())
print(mensagem.swapcase())
print(mensagem.strip()) #Remove espalos extras no inicio e no fim da variavel
print(mensagem.rstrip()) #Remove espalos extras no inicio da variavel
print(mensagem.lstrip()) #Remove espalos extras no fim da variavel
print(mensagem.replace('Minas Gerais', 'Sao Paulo')) #Substitui as palavras
print(mensagem.find('G')) # Index da posição
print(mensagem.count("i"))  # total de ocorrencias
print(mensagem[::-1])  # "nohtyP"


#String Format
nome = "Demetrius"
idade = 31
print("Meu nome é {} e tenho {} anos.".format(nome, idade))

print(f"Meu nome é {nome} e tenho {idade} anos.")
# "Meu nome é Demetrius e tenho 31 anos."

'''
upper()	Converte para maiúsculas
lower()	Converte para minúsculas
capitalize()	Primeira letra maiúscula
title()	Primeira letra de cada palavra maiúscula
strip()	Remove espaços extras
replace()	Substitui um texto por outro
find()	Encontra a posição de um texto
count()	Conta quantas vezes aparece
split()	Divide em uma lista
join()	Junta elementos em string'''