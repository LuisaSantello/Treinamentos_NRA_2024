
def palindromo(frase):
    frase = frase.replace(' ','')
    frase = frase.lower()
    i = 0
    ordem = []
    ordemi = []
    # frasei = []
    # frasei = frase[::-1]
    for i in range(0,len(frase)-1,1):
      #ordem[i] = frase[i]
      ordem.append(frase[i])

    for a in range(len(frase)-1, 0, -1):
       # ordemi[a] = frase[a]
        ordemi.append(frase[a])
    z = 0
    x = 0
    while z<len(frase)-1:
        if ordem[z]!=ordemi[z]:
            x =1
           # print('Nao e um palindromo')
           # break
        z = z+1
        #if ordem == ordemi:
            #print('Essa frase e um palindromo')
    if x == 1:
        print('A frase nao e um palindromo')
    else:
        print('A frase e um palindromo')


dig = input('Digite uma frase: ')
palindromo(dig)