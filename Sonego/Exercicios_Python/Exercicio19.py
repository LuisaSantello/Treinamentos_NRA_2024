lista_geral = []
lista_par = []
lista_impar = []
valor = 0
while True:
    valor = int(input('Digite um valor: '))
    if (valor < 0):
        break
    lista_geral.append(valor)
    if(valor % 2):
        lista_impar.append(valor)
    else:
        lista_par.append(valor)

print(lista_geral, lista_par, lista_impar)