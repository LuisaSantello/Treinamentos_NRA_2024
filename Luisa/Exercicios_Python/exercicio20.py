jogadores = dict()
inf = []

while True:
    nome = input('Qual o nome do jogador? ')
    partidas = int(input('Quantas partidas ele jogou?'))
    gols = int(input('Quantos gols o jogador {} fez?'.format(nome)))
    n = partidas * gols
    inf.append(partidas, gols, n)
    jogadores.update({nome, inf})
    resp = input('Quer adicionar mais um jogador?')
    if resp == 'nao':
        break
  

print(jogadores)