mais_velho_idade = 0
mulheres_abaixo20 = 0
media_idade = 0
numero_pessoas = 4
for i in range(numero_pessoas):
    Nome = input('Insira o nome da pessoa: ')
    Idade = int(input('Insira a idade da pessoa: '))
    Sexo = input('Insira o sexo da pessoa: ')
    if(Sexo == 'masculino' and mais_velho_idade < Idade):
        mais_velho_idade = Idade
        mais_velho_nome = Nome
    if(Sexo == 'feminino' and Idade < 20):
        mulheres_abaixo20 += 1
    media_idade += float(Idade / numero_pessoas)
print('A media de idade é: {}\nO nome do homem mais velho é: {}\nO número de mulheres abaixo de 20 anos é:{}\n'.format(media_idade, mais_velho_nome, mulheres_abaixo20))