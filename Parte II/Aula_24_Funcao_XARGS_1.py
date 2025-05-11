#Usando multiplos argumentos com XARGS no Python

# função que recebe uma lista de numeros e soma. 

#*ARGS

def soma(*numeros):
    resultado =0
    for i in numeros:
        resultado += i
    return resultado


numeros = (1,2,3,4,5,6,7,8,9)

print(soma(*numeros))




# Somando uma lista de objetos
def soma(*numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    return resultado

numeros = [1,2,3,4,5,6,7,8,9]
print(soma(*numeros))  # Saída: 45
