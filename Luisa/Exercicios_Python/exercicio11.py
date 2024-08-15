valor=int(input('Informe o valor que deseja sacar'))
c = valor//50
valor = valor%50
v = valor//20
valor = valor%20
d = valor//10
u = valor%10
print('Sera sacado {0} cedulas de cinquenta reais, {1} cedulas de vinte reais, {2} cedulas de dez reais e {3} moedas de um real'.format(c,v,d,u))
