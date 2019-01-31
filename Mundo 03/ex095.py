jogador = {}
jogadores = []
while True:
    jogador['Nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    gols = []
    for c in range(partidas):
        gol = int(input(f'Quantas gols na partida {c + 1}: '))
        gols.append(gol)
    jogador['Gols'] = gols
    jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 16)
print(f'{"Cód.":<11}{"Nome":<15}{"Gols":<15}{"Total":<15}')
print('-' *48)
for k, v in enumerate(jogadores):
    print(f'{k:<11}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' *48)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    for k, v in enumerate(jogadores):
        if busca == k:
            print(f'LEVANTAMENTO DO JOGADOR: {v["Nome"]}')
            jogo = 1
            for d in v['Gols']:
                print(f'No jogo {jogo} fez {d} gols.')
                jogo += 1
            print('-' * 48)
    if busca == 999:
        break
print('-' *48)
print('<<< TERMINADO >>>')


















