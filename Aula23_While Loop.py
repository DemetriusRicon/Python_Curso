valor = int(input('Digite o valor do seu produto '))


while valor >20:
    valor = valor - (valor*0.10)
    print(f'O valor com desconto é R$ {valor}')
    break