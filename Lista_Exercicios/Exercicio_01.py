# Given two integer numbers, write a Python program to return their product 
# only if the product is equal to or lower than 1000. 
# Otherwise, return their sum.

'''
valor1 = int(input("Digite o primeiro numero "))
valor2 = int(input("Digite o segundo numero "))

if valor1 * valor2 <= 1000:
  print (f'Seu resultado é menor que 1000 e foi multiplicado, valor final : {valor1 * valor2}')
else : 
  print(f'Seu resultado é maior que 1000 e foi somado :{valor1 + valor2}')

'''

def sumormulti (valor3,valor4 ):
  if valor3 * valor4 <= 1000:
    print (f'Seu resultado é menor que 1000 e foi multiplicado, valor final : {valor3 * valor4}')
  else : 
    print(f'Seu resultado é maior que 1000 e foi somado :{valor3 + valor4}')

sumormulti(10,10)