Valor_casa = float(input('Qual o valor da casa? '))
Salario = float(input('Qual o salário? '))
Anos_financiamento = float(input('Em quantos anos a casa será paga? '))
Parcela_mensal = Valor_casa/(12 * Anos_financiamento)

if((Parcela_mensal + 10e-13) > Salario*0.3):
    print('Emprestimo Negado!')
    quit()

print('Emprestimo Aceito!')

