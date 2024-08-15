valor=float(input('Qual o valor da casa?'))
salario=float(input('Qual seu salario?'))
anos=int(input('Em quantos anos pretende pagar a casa?'))
prestacao=valor/(12*anos)
if prestacao<=(0.3*salario):
    print('{}'.format(prestacao))
    print('Emprestimo aprovado')
else:
    print('{}'.format(prestacao))
    print('Emprestimo negado')
