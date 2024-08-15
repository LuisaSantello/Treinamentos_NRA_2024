l1= float(input('Digite o tamanho do primeiro lado:'))
l2 = float(input('Digite o tamanho do segundo lado:'))
l3 = float(input('Digite o tamanho do terceiro lado:'))

if l1<l2+l3 and l2<l1+l3 and l3<l2+l1:
    print('As tres retas podem formar um triangulo')
    if l1!=l2 and l1!=l3 and l2!=l3:
        print('As retas formam um triangulo escaleno')
    elif l1==l2 or l1==l3 or l2==l3:
        if l1==l2 and l1==l3:
            print('As tres retas formam um triangulo equilatero')
        else:
            print('As tres retas formam um triangulo isosceles')  
else:
    print('As tres retas nao podem formar um triangulo')

