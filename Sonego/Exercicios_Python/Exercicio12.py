Nome = input('Digite seu nome: ')
print(Nome.upper(), Nome.lower())
print('Numero de letras: {}'.format(len(Nome) - Nome.count(' ')))
print(Nome.split(' ')[0])