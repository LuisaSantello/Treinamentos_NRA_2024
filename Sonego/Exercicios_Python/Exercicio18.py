lista = []
for i in range(5):
    valor = float(input('Digite um valor: '))
    lista.append(valor)

print('O maior valor é: {} e seu respectivo indice: {}'.format(max(lista), lista.index(max(lista))))
print('O menor valor é: {} e seu respectivo indice: {}'.format(min(lista), lista.index(min(lista))))