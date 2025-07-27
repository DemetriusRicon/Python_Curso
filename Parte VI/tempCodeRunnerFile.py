try:
    valor = int(input('Digite o valor do produto '))
except ValueError:
    print('Favor, Digite um numero inteiro')
else :
    print("O usuario digitou o valor aderente a regra")
    resultado = valor * 2
    print(resultado)
