soma = 0
for i in range (0,6,1):
    numero = int(input('Digite um numero inteiro'))
    if numero%2 == 0:
        soma = soma + numero 
print('A soma dos numeros pares digitados e {}'.format(soma))
