def leiaInt(Frase):
    Entrada = input(Frase)
    if (not Entrada.isnumeric()):
        return print('Não é inteiro')
    Entrada = int(Entrada)
    return Entrada

inteiro = leiaInt('leia um inteiro n: ')