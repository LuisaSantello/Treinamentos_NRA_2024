Peso = float(input('Insira o peso, em kg: '))
Altura = float(input('Insira a altura, em metros: '))

IMC = Peso/(Altura**2)

if(IMC < (18.5 + 10e-13)):
    print('Abaixo do Peso')
    quit()

if(IMC < (25 + 10e-13)):
    print('Peso Ideal')
    quit()

if(IMC < (30 + 10e-13)):
    print('Sobrepeso')
    quit()

if(IMC < (40 + 10e-13)):
    print('Obesidade')
    quit()

print('Obesidade Mórbida')