#Criar uma classe 
class Funcionario:
   def __init__(self ,nome,sobrenome, data_nascimento):
      self.nome = nome
      self.sobrenome = sobrenome
      self.data_nascimento = data_nascimento
   
   #Semelhante ao ToString do Java onde concatenamos as informações para saída
   def mostra_dados(self):
        return (f'{self.nome} {self.sobrenome} - {self.data_nascimento}')

#Criando um objeto
usuario1 = Funcionario('Lucas', 'Magno', '01-01-1901')
usuario2 = Funcionario('Maria', 'Miranda', '01-01-1999')

#Acessando uma função da classe
print(usuario1.mostra_dados())
print(usuario2.mostra_dados())


#---
print (Funcionario.mostra_dados(usuario1))


# #Criando os parametros do usuario 1
# usuario1.nome = 'Demetrius'
# usuario1.sobrenome = 'Ricon'
# usuario1.data_nascimento = '12-12-2012'

# #Criando os parametros do usuario 2
# usuario2.nome = 'Ketlen'
# usuario2.sobrenome = 'Santos'
# usuario2.data_nascimento = '12-12-2021'


