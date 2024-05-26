class Pessoa:
    ano_atual = 2024
    falando = False
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        print(f'{self.nome} chegou!')
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} está falando')
            return
        print(f'{self.nome} está comendo {alimento}')

    def parar_comer(self):
        self.comendo = False
        print(f'{self.nome} parou de comer')

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} está comendo e não pode falar')
            return
        print(f'{self.nome} está falando de {assunto}')

    def parar_falar(self):
        self.falando = False
        print(f'{self.nome} parou de falar')
    
    def ano_nascimento(self):
        return self.ano_atual - self.idade 

Jose = Pessoa('Jose', 18, False, True)
Jose.parar_falar()
Jose.comer('Arroz')
Jose.parar_comer()
Jose.falar('Rosbife')