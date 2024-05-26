Largura = float(input('Qual é a largura da parede? '))
Altura = float(input('Qual é a altura da parede? '))
Area = Largura * Altura
Tinta_litro_por_area = 2
Quantidade_tinta = Area/Tinta_litro_por_area
print('Serão necessários: ', Quantidade_tinta, 'litros de tinta para pintar a parede')