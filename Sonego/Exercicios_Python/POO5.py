class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def valor_compra(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

carrinho1 = CarrinhoDeCompras()
produto1 = Produto('Arroz', 'R$ 7.30')

carrinho1.listar_produtos()
carrinho1.inserir_produto(produto1)
carrinho1.listar_produtos()