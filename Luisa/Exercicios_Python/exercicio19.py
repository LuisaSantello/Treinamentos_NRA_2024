x = True 
lista = []
while x == True:
    y = int(input("Digite um numero: "))
    if y >=0:
        lista.append(y)
    if y<0:
        break
   

pares = []
impares = []
for i in range(0, len(lista), ):
    if (lista[i]%2) == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(lista, pares, impares)