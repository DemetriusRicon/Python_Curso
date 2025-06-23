dados_aluno = {
    'nome': 'Ana',
    'idade': 20,
    'nota_final': 'A',
    'aprovacao': True,
    'Materias': [
        'Matemática',
        'Português',
        'Biologia',
        'Química',
        'Física',
        'História',
        'Geografia',
        'Inglês',
        'Artes',
        'Educação Física'
    ]
}

print(dados_aluno)

print(dados_aluno.get('Materias'))



dicionario = {'nome': 'Vinícius ', 'idade': 29, 'empresa': 'PythonAcademy'}

# Atualiza dados
dicionario['idade'] = 30
dicionario['empresa'] = ' Academia Python'