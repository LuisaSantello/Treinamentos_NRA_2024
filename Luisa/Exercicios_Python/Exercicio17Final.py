def gerar_5():
    from random import randrange
    lista = []
    for i in range (0,5,1):
        lista.append(randrange(1000))
    return lista

l = tuple(gerar_5())
n = len(l)

maximo = max(l)
minimo = min(l)
print(l, maximo, minimo)