class Caneta:
    def __init__(self, marca, cor):
        self.__marca = marca
        self.__cor = cor
    
    def escrever(self):
        print(f'Caneta {self.__marca} está escrevendo na cor {self.__cor}')
    
class Escritor:
    def __init__(self, caneta):
        self.caneta = caneta

caneta1 = Caneta('Bic', 'Preta')
escritor1 = Escritor('Machado')

escritor1.caneta = caneta1
escritor1.caneta.escrever()