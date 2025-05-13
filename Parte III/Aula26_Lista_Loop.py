#For Loops


valores_lista = [10,20,30,40,50,60,70,80,90,100]

for i in valores_lista:
    print (f'Os valores da lista são valores {i}')



cor_cliente = input('Digite a cor desejada: ').lower()

cores = ['azul', 'branco', 'verde', 'amarelo']

if cor_cliente in cores:
    print('Em estoque - disponível para preparação')
else:
    print('Sem estoque')
