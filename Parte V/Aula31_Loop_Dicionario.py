dados_aluno = {
    'nome': 'Ana',
    'idade': 20,
    'nota_final':'A',
    'aprovacao': True
}


for chave in dados_aluno.keys():
    print(chave)

for item in dados_aluno.items():
    print(item)

for valores in dados_aluno.values():
    print(valores)

for chave, valores in dados_aluno.items():
    print(chave, valores)



