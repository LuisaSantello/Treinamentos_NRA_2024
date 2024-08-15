hvelho = 0
munder = 0
soma = 0
for i in range(0,4,1):
    nome = input('Qual o nome da pessoa {}'.format(i))
    idade = int(input('Qual a idade da pessoa {}'.format(i))) 
   # idade = int(input('Qual a idade da pessoa?'))
    sexo = int(input('Qual o sexo da pessoa {}, digite 1 para homem e 2 para mulher'.format(i)))
    soma = soma + idade
    if sexo == 2 and idade<20:
        munder = munder + 1
    if sexo == 1 and hvelho<idade:
        hvelho=idade 
        nomehvelho = nome
media = soma/4
print('A media das idades e {}, o nome do homem mais velho e {} e existem {} mulheres menores de 20 anos'.format(media, nomehvelho, munder))
