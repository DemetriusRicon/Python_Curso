nome = 'Demetrius Ricon'
numero = 0


while numero <=  10:
    print (nome)


valor = 100
custo = 20
dia = 1
while valor > custo :
    dia+=1
    print(f'O valor comprado foi de {valor} no dia {dia}')
    valor -=5



# Exemplo: Imprimir um losango na consola
altura = 5
caracter = "*"

# Parte superior do losango
for i in range(altura):
    print(" " * (altura - i - 1) + caracter * (2 * i + 1))

# Parte inferior do losango
for i in range(altura - 2, -1, -1):
    print(" " * (altura - i - 1) + caracter * (2 * i + 1))