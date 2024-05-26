Reta_1 = float(input('Insira a primeira reta: '))
Reta_2 = float(input('Insira a segunda reta: '))
Reta_3 = float(input('Insira a terceira reta: '))

if((Reta_1 <= abs((Reta_2 - Reta_3))) or (Reta_1 >= (Reta_2 + Reta_3))):
    print('Não é possível formar um triângulo com essas retas')
    quit()

if((abs((Reta_1 - Reta_2)) < 10e-13) and (abs((Reta_2 - Reta_3)) < 10e-13)):
    print('O triângulo é equilátero')
    quit()

if(abs(((Reta_1 - Reta_2)) < 10e-13) or (abs((Reta_1 - Reta_3)) < 10e-13) or (abs((Reta_2 - Reta_3)) < 10e-13)):
    print('O triângulo é isóceles')
    quit()

print('O triângulo é escaleno')