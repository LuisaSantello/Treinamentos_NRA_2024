Teste = 0
lista_jogadores = []
Total_gols_time = 0

while (1):
    Teste = input('Gostaria de adicionar um jogador?:\n')
    if((Teste == 'Não') | (Teste == 'Nao') | (Teste == 'não') | (Teste == 'nao')):
        break
    Nome = input("Nome do jogador:\n")
    Partidas = int(input("Partidas jogadas:\n"))
    Gols_Partida = []
    Total_gols = 0
    for i in range(Partidas):
        gol_na_partida = int(input("Gols na partida {}:\n".format(i+1)))
        Gols_Partida.append(gol_na_partida)
        Total_gols += gol_na_partida
    Jogador = {'Nome': Nome, 'Partidas': Partidas, 'Gols_Partida': Gols_Partida, 'Total_Gols': Total_gols}
    lista_jogadores.append(Jogador)
    Total_gols_time += Total_gols

print(Total_gols_time)

for i in lista_jogadores:
    print(i)