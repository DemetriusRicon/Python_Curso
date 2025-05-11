#Tipos de função 


def imprime_nome(nome):
    print(f'Ola {nome}')

imprime_nome('Maria')


def imprime_nome2(nome):
    return f'Ola {nome}'

print(imprime_nome2('Demetrius'))


mensagem = imprime_nome2("Lucas")
print(mensagem.upper())  # -> OLA LUCAS

'''
| Característica        | `imprime_nome`     | `imprime_nome2`       |
| --------------------- | ------------------ | --------------------- |
| Usa `print` dentro    | Sim                | Não                   |
| Usa `return`          | Não                | Sim                   |
| Reutilização do valor | Não                | Sim                   |
| Retorna algo?         | `None` (implícito) | String (`'Ola nome'`) |
| Testável em código    | Difícil            | Fácil                 |
'''



