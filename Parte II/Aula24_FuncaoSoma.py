def somar_numero():
    num1 = 10
    num2 = 20
    resultado = num1+num2
    print(resultado)


somar_numero()



def funcao_estranha():
    print('Essa é uma função estranha')

funcao_estranha()


#Número par ou ímpar - Crie uma função eh_par(numero) que retorna True se o número for par e False caso contrário.
numero = int(input(' Digite um numero para verificacao '))

def calcular_par_impar(numero):
    if numero %2 == 0:
        print ('Voce escolheu par')
    else :
        print ('Voce escolheu impar')

calcular_par_impar(numero)

# Maior número - Escreva uma função maior(a, b) que retorna o maior entre dois números.

a=1
b=2

def calcular_maior(a,b):
    resultado = (f'O primeiro valor {a} é maior que o segundo valor {b}') if a>b else (f'O seghundo valor {b} é maior que o primeiro valor {a}')
    print(resultado)

calcular_maior(a,b)
