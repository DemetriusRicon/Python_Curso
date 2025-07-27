
'''
try, except e finally são usados para tratar erros (exceções) e garantir que certas ações sejam executadas, mesmo que ocorra um erro.

Explicação

try: Você coloca o código que pode gerar um erro dentro do bloco try.

except: Se ocorrer um erro dentro do try, o Python pula para o bloco except, onde você pode tratar o erro.

finally: O bloco finally sempre é executado, independentemente de ter ocorrido um erro ou não. É útil para liberar recursos, fechar arquivos, etc.
'''

# Como fazer um bom tratamento de erros. 

# letras = ['a', 'b','c']
# print(letras[3])
# Traceback (most recent call last):
#   File "c:\Users\DEV\Documents\Python Scripts\Python_Curso\Parte VI\Aula38_Erros.py", line 5, in <module>
# print(letras[3])
#   ~~~~~~^^^
# IndexError: list index out of range

try: 
    letras = ['a','b','c']
    print(letras[3])
except IndexError:
    print ('Indice nao existente na lista')



try:
    valor = int(input('Digite o valor do produto '))
except ValueError:
    print('Favor, Digite um numero inteiro')


try:
    valor = int(input('Digite o valor do produto '))
except ValueError:
    print('Favor, Digite um numero inteiro')
else :
    print("O usuario digitou o valor aderente a regra")
    resultado = valor * 2
    print(resultado)


try:
    valor = int(input('Digite o valor do produto '))
except ValueError:
    print('Favor, Digite um numero inteiro')
finally :
    print("O usuario digitou o valor aderente a regra")
    resultado = valor * 2
    print(resultado)

