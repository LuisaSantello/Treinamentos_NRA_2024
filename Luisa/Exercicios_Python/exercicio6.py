x=1
y=2
while x<=10:
    print(y)
    y = y + 2 
    x = x + 1
else:
    print('Quer continuar imprimindo?')
    resp = int(input('responda 1 para SIM ou 2 para NAO'))
    if resp == 1:
        while x<=15:
            print(y)
            y = y +2
            x=x+1