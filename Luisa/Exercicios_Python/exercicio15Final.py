def maior(*num):
    print('Analisando os valores passados...')
    i = 0
    #contador i 
    #x vai ser o maior numero
    x = 0
    for valor in num:
        print(valor)
        if valor>x:
            x = valor
        i = i + 1
    print('Foram informados {} valores'.format(i))
    print('O maior valor e', x)

maior(10, 20, 80, 5, 3, 2, 18, 60, 91, 2)