dias = int(input('Por quanto dias o carro foi alugado?'))
km = float(input('Quantos quilometros o carro percorreu?'))
pagar = float(dias*60) + km*0.15
print('o total a ser pago pelo carro e', pagar)