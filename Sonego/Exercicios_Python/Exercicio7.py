Adulto = 0
Homens = 0
Mulheres_abaixo20 = 0
Escolha = 'sim'

while (Escolha == 'sim'):
    Sexo = input('Qual é o sexo da pessoa?\n')
    if(Sexo == 'masculino'):
        Homens += 1
    Idade = int(input('Qual a idade da pessoa?\n'))
    if(Idade > 18):
        Adulto += 1
    if(Sexo == 'feminino' and Idade < 20):
        Mulheres_abaixo20 += 1

    Escolha = input('Continuar?\n')

print('Numero de adultos: {}\nNúmero de homens: {}\nNúmero de mulheres abaixo de 20 anos: {}\n'.format(Adulto, Homens, Mulheres_abaixo20))