def IsPalindromo(frase):
    frase = frase.lower().replace(' ', '')
    for i in range(len(frase)//2):
        if (frase[i] != frase[-(i+1)]):
            print('Não é palíndromo')
            return
    return print('É palíndromo')

frase = 'anotaram a data da maratona'
IsPalindromo(frase)
