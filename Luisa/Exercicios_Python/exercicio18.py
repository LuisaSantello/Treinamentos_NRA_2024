lista = []
for i in range(0,5,):
    lista.append(int(input('Digite o valor numerico da posicao {}: '.format(i+1))))

print(lista)
maximo = max(lista)
minimo = min(lista)
pmaximo = lista.index(maximo)
pminimo = lista.index(minimo)
print('O maior valor e: {0} e sua posicao e: {1}. O menor valor e: {2} e sua posicao e: {3}'.format(maximo, pmaximo, minimo, pminimo))