#Unpacking Lists

cod_produto = [1,2,3,4,5]

codigo = cod_produto[3]

print(codigo)


#Da pra desempactorar uma lista de dados originalmente maior que a quantidade de variaveis que eu preciso.
#Usando o * (semelhante ao *args) eu consigo colocar o 'resto' dos valores dentro de uma variavel que me apresenta o resto. 
cod1,cod2,cod3,cod4,*outros = cod_produto

print(outros)



#Exemplo de reforço
a, b, *resto = [10, 20, 30, 40, 50]
print(a)   
print(b)      
print(f' O resto da lista : {resto}')