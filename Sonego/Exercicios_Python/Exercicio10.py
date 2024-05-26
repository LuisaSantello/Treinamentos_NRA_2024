numero = 0

while True:
    numero = int(input('Digite quais numeros deseja saber a tabuada: '))
    if numero < 0:
        break
    for i in range (11):
        print(numero*i)