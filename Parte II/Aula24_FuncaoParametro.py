'''
Sobrescrita de parametros, muitas das vezes queremos passar parametros em funções que ja podem ter um valor default,
para nao se ater a essa necessidade, podemos passar valores default para argumentos dentro da função.

#def nome_funcao(valor1, valor2= 'valor_padrao')

Manter a ordem é necessaria

Regra de Ouro - Parametros non default sempre são passados primeiro. 
O que muda de valor vem primeiro
O que nao muda de valor vem depois
'''
 

def boas_vindas (nome,quantidade):
    print(f'Ola {nome}')
    print(f'Temos {quantidade} laptops em estoque')