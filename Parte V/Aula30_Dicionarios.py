#Dicionários em Python são estruturas de dados que armazenam pares de chave e valor. 
#Eles permitem acessar valores rapidamente usando a chave correspondente, em vez de um índice numérico como nas listas.

dados_aluno = {
    'nome': 'Ana',
    'idade': 20,
    'nota_final':'A',
    'aprovacao': True
}

print(dados_aluno)
print(dados_aluno['idade'])

dados_aluno['nome'] = 'Jose'
print( dados_aluno)

dados_aluno.update({'endereco': 'Setor Brasilia'})
print(dados_aluno)


#buscando via Get
print(dados_aluno.get('Setor', 'Nao encontrado'))

#removendo 
del dados_aluno['aprovacao']

print(dados_aluno)