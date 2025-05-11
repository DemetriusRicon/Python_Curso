from datetime import date

ano_atual = date.today().year

ano = int(input('Digite seu ano de nascimento '))
idade_atual = ano_atual - ano
print ('Sua idade é ', idade_atual)