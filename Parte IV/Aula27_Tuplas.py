#Armazena mais de uma informação em variavel
# Não alteravel
#Mantem a sequencia dos dados. 

#Vamos ver brevemente a diferença entre lista e Tuplas

lista = [1,2,3,4,5]
tupla = (1,2,3,4,5)


print (lista)
print('')
print(tupla)

#A apresentação final dos dados se dá pela diferença de um parentese 

'''Não é possivel em Tuplas usar Append, o que significa que uma vez que voce criar uma lista
 ja era! Ela vai ficar daquele jeito pra sempre. 

 É possivel desempacotar uma tupla de forma inversa, sem a necessidade de vir definindo variavel a variavel cada posição
'''

a,b,c,d,e = tupla

print (f"O valor de A  : {a}")
print (f"O valor de A  : {b}")
print (f"O valor de A  : {c}")
print (f"O valor de A  : {d}")
print (f"O valor de A  : {e}")


#Chamando somente um valor da tupla
print(tupla[2])
