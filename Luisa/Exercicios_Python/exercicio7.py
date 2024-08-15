
while (True):
    sexo = input('Qual o sexo?')
    idade = int(input('Digite a idade:'))
    h = 0
    munder = 0
    i = 0
    if idade>18:
        i = i +1
    if sexo == 'homem':
        h = h + 1
    if sexo=='mulher' and idade<20:
        munder = munder + 1
    resp = input('Quer continuar o cadastro?')
    if resp == 'NAO':
        break 
    if resp == 'sim':
        continue 

print('{} pessoas maiores de 18 anos foram cadastradas, {} homens foram cadastrados e {} mulheres com menos de 20 anos foram cadastradas'.format(i, h, munder))

