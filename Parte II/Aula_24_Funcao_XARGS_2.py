#Função que armazena dados identificando parametros
#Args e Kwargs

'''
| Característica            | `*args`                                  | `**kwargs`                                     |
| ------------------------- | ---------------------------------------- | ---------------------------------------------- |
| Nome técnico              | Argumentos posicionais variáveis         | Argumentos nomeados variáveis                  |
| Símbolo                   | `*`                                      | `**`                                           |
| Tipo de dado recebido     | Tupla (`tuple`)                          | Dicionário (`dict`)                            |
| Uso comum                 | Vários valores sem nome (como `1, 2, 3`) | Vários pares `chave=valor` (como `x=10, y=20`) |
| Como declarar             | `def funcao(*args):`                     | `def funcao(**kwargs):`                        |
| Como acessar              | Loop: `for a in args`                    | Loop: `for chave, valor in kwargs.items()`     |
| Como passar para a função | `funcao(1, 2, 3)`                        | `funcao(nome="Ana", idade=30)`                 |
| Como desempacotar         | `funcao(*lista)`                         | `funcao(**dicionario)`                         |
'''

def veiculos_agn(*carro):
    return carro

primeiro_modelo = veiculos_agn('GM - ONIX', 'Branca', 1.0)
print(veiculos_agn(primeiro_modelo))



def veiculos_agn2(**carro):
    return carro

print(veiculos_agn2(modelo = 'Onix', marca= 'GM', ano ='1997', motor = '1.0'))
