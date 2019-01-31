from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados:')
sleep(0.8)
jogadores = {'Jogador 01': randint(1, 6),
             'Jogador 02': randint(1, 6),
             'Jogador 03': randint(1, 6),
             'Jogador 04': randint(1, 6)
             }
ranking = {}
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.8)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()
print('=== RANKING DOS JOGADORES ===')
print(ranking)
for x in range(0, len(ranking)):
    if x == 0:
        print(f'{contador}° Lugar: {ranking[x][0]} com {ranking[x][1]}.')
    elif ranking[x][1] == ranking[x - 1][1]:
        print(f'{contador}° Lugar: {ranking[x][0]} com {ranking[x][1]}.')
    else:
        contador += 1
        print(f'{contador}° Lugar: {ranking[x][0]} com {ranking[x][1]}.')
    sleep(0.8)




