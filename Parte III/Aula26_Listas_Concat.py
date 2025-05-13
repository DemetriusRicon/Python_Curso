# Replicando uma lista 

numeros = [1,2,3,4]

#Replica  os valores de uma lista em sequencia com base no multiplicador
novalista = numeros *4

print(novalista)


#Concatenando uma lista
alfabeto =['a','b','c','d']

final = numeros + alfabeto
print(final)


#  * com listas → replica os elementos da lista.
#  + com listas → concatena listas.
# | Operação                | O que faz                                         | Modifica a lista original? | Retorna o quê?   |
# | ----------------------- | ------------------------------------------------- | -------------------------- | ---------------- |
# | `lista1 + lista2`       | Cria uma **nova lista** com os elementos das duas | ❌ **Não**                  | ✅ Uma nova lista |
# | `lista1.extend(lista2)` | **Adiciona os elementos** de `lista2` à `lista1`  | ✅ **Sim**                  | ❌ Retorna `None` |

numeros.extend(alfabeto)
print(numeros)


#Listas dentro de uma lista

numero =[[1,2,3],[4,5,6]]
print(numero[0][2])