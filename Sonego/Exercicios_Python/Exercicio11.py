Valor = int(input('Qual o valor a ser sacado?\n'))
Notas_50 = int(Valor/50)
Notas_20 = int((Valor % 50) / 20)
Notas_10 = int(((Valor % 50) % 20) / 10)
Notas_1 = int((((Valor % 50) % 20) % 10))

print('Cédulas de 50 reais: {}\nCédulas de 20 reais: {}\nCédulas de 10 reais: {}\nCédulas de 1 real: {}'.format(Notas_50, Notas_20, Notas_10, Notas_1))