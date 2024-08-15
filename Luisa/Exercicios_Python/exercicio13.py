frase = input('Digite uma frase')
print(frase.count('a',0, len(frase)))
frase = frase.replace(' ','')
#print(frase)

print(frase.find('a'))

for i in range(len(frase), 0, -1):
    if frase.count('a', 0, len(frase))!=0:
        if 'a' in frase:
            print(i)
           
            break
    else:
        print('nao ha "a" nessa frase')
