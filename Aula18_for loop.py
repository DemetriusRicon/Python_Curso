

#imprimir numeros em um loop
for valor in range(5):
    print(f"O valor atual é {valor}")


#imprimir numeros em um loop com passo
# INICIO , FIM E PASSO (pulo)
for valor in range(1,400,2):
    print(f"O valor atual com passo esta em {valor}")


frase = 'Python é uma linguagem de programação'
for letra in frase:
    print(letra)    

#Iterando sobre uma String
frase = 'Python é uma linguagem de programação'
for letra in frase:
    print(f"{letra} : Esta dentro da frase") 



#Usando um for e um IF para iterar sobre um processo. 
#Break encerrando o loop
compra_confirmada = True
dados_compra = 'Compra no valor de 10,00 e entrega confirmada'

for enviar_email in range(3):
    if compra_confirmada:
        print (dados_compra)
        print ('Detalhes enviados para o seu email')
        break
    else:
        print("Falha na comnunicação da compra")



#Nested Loop = Loop Aninhado
for numero in range(5):
    print (f"Esse e o numero inicial", numero)
    for numero2 in range(5):
        print(numero,numero2)


def construir_piramide(n):
          for i in range(n):
              print(' ' * (n - i - 1), end='')
              for j in range(i + 1):
                  print(j + 1, end=' ')
              print()
  
construir_piramide(3)


print('-' * 5) 

