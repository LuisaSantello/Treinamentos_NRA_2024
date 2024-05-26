dias_alugado = int(input('Há quantos dias o carro foi alugado? '))
quilometros_percorridos = float(input('Quantos quilômetros o carro percorreu? '))
preço = 60*dias_alugado + 0.15*quilometros_percorridos
print('O preço a pagar será de: {preco} Reais'.format(preco = preço))