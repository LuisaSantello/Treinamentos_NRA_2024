frase = input('Digite uma frase: ')
frase = frase.lower()
numero_aparicoes = frase.count('a')
primeira_aparicao = frase.find('a')
ultima_aparicao = primeira_aparicao
for i in range (numero_aparicoes - 1):
    ultima_aparicao = frase.find('a', (ultima_aparicao + 1))
print('Número de aparições da letra "a": {}\nPosição em que "a" aparece pela primeira vez: {}\nPosição em que "a" aparece pela última vez: {}'.format(
numero_aparicoes, primeira_aparicao, ultima_aparicao))