import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF8')

renda_salario_5mil = False
nome_limpo = False

if renda_salario_5mil or nome_limpo:
    print('Financiamento aprovado')
else :
    print('Financiamento negado, validações contestadas')