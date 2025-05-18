'''
Array em Python é uma estrutura de dados que armazena uma coleção de elementos do mesmo tipo, de forma sequencial na memória. Diferente das listas, os arrays do módulo `array` são mais eficientes em termos de uso de memória e desempenho quando você precisa armazenar muitos dados numéricos do mesmo tipo (por exemplo, apenas inteiros ou apenas floats).

Para usar um array em Python, você precisa importar o módulo `array` e especificar o tipo de dado que ele irá armazenar, usando um código de tipo (por exemplo, `'i'` para inteiros, `'f'` para floats). Exemplo:

````python
from array import array

# Criando um array de inteiros
meu_array = array('i', [1, 2, 3, 4, 5])
print(meu_array)
````

Principais características:
- Todos os elementos devem ser do mesmo tipo.
- Mais eficiente que listas para grandes volumes de dados numéricos.
- Suporta operações como adicionar, remover e acessar elementos por índice.

Use arrays quando precisar de desempenho e trabalhar apenas com tipos de dados homogêneos. Para dados de tipos variados, prefira listas.
'''

from array import array

meu_array = array('i', [100, 2, 30, 4, 5])
print(meu_array)
meu_array = array(meu_array.typecode, sorted(meu_array))
print(meu_array)


typecodes = {
    'b': 'signed char (inteiro, 1 byte)',
    'B': 'unsigned char (inteiro sem sinal, 1 byte)',
    'u': 'unicode character (caractere unicode, 2 bytes) [descontinuado em Python 3.3+]',
    'h': 'signed short (inteiro curto, 2 bytes)',
    'H': 'unsigned short (inteiro curto sem sinal, 2 bytes)',
    'i': 'signed int (inteiro, 2 ou 4 bytes)',
    'I': 'unsigned int (inteiro sem sinal, 2 ou 4 bytes)',
    'l': 'signed long (inteiro longo, 4 bytes)',
    'L': 'unsigned long (inteiro longo sem sinal, 4 bytes)',
    'q': 'signed long long (inteiro longo longo, 8 bytes)',
    'Q': 'unsigned long long (inteiro longo longo sem sinal, 8 bytes)',
    'f': 'float (ponto flutuante, 4 bytes)',
    'd': 'double (ponto flutuante duplo, 8 bytes)'
}

for code, desc in typecodes.items():
    print(f"'{code}': {desc}")