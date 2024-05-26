Escolha = 'sim'
Comeco, Razao = 3, 2
for i in range(9):
    print(Comeco + i*Razao)
while Escolha == 'sim':
    i += 1
    print(Comeco + i*Razao)
    Escolha = input('Gostaria de mostrar mais um termo?\n')