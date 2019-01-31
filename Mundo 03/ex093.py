jogador = {}
jogador['Nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
gols = []
for c in range(partidas):
    gol = int(input(f'Quantas gols na partida {c + 1}: '))
    gols.append(gol)
jogador['Gols'] = gols
jogador['Total'] = sum(gols)
print('-=-' * 18)
print(jogador)
print('-=-' * 18)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 18)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, c in enumerate(jogador['Gols']):
    print(f'=> Na partida {i + 1}, fez {c} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')


