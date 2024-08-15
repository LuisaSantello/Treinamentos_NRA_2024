#n = int(input('Digite um numero: '))
#print('Voce acabou de digitar o numero ',n)

def leiaInt():
    numero = 0
    x = input("Digite um numero")
    if x.isnumeric() == True:
        numero = int(x)
        print('Voce digitou o numero', numero)
    else: 
        print('ERRO! Digite um numero valido')
    
def leiaAteInt():
    flag = False
    while 1:
        numero = 0
        x = input("Digite um numero")
        if x.isnumeric() == True:
            numero = int(x)
            print('Voce digitou o numero', numero)
            flag = True 
        else: 
            print('ERRO! Digite um numero valido')
        if flag == True:
            break
# SEM O BREAK 
#           while flag == False:

leiaAteInt()
