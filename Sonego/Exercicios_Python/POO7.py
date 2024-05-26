class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando')
    
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando')

Pessoa1 = Pessoa('Pessoa1', 24)
Aluno1 = Aluno('Aluno1', 14)
Cliente1 = Cliente('Cliente1', 32)

Aluno1.falar()
#Cliente1.estudar()
#Pessoa1.estudar()
#Pessoa1.falar()