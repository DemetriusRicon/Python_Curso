#Uma função lambda em Python é uma função anônima, ou seja, uma função sem nome, definida usando a palavra-chave lambda. 
#Ela é geralmente usada para criar funções pequenas e simples de forma concisa, especialmente quando você precisa passar uma função como argumento para outra função
# (por exemplo, em funções como map, filter ou sorted)

#Exemplo de Soma

def soma(x):
    return x +10

print(f' O resultado da funcao de soma é : {soma(10)}')


#Usando Lambda

somar_10 = lambda x,y: x + 10 * y
print(somar_10(2,5))

# LAMBDA ARGUMENTO : EXPRESSAO

lista_grande = [1,2,3,4,5,6,7,8,9,10]

quadrado = list(map(lambda x:x**2,lista_grande))
                
print(f'O Resultado da lista ao quadrado e {quadrado}')


#Lambda dentro de uma função

def somar_2(argumento):
    calculo_rapido = lambda argumento : argumento +10
    return calculo_rapido(argumento) * 4

print(somar_2(10))