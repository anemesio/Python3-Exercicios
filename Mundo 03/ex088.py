from random import randint
print('-' * 40)
print(f'{"JOGOS PARA MEGASENA":^40}')
print('-' * 40)
jogos = []
auxiliar = []
index = cont =  0
qtdde = int(input('Quantos jogos  você quer que eu sorteie? '))
print('-=-' * 3, end=' ')
print(f'SORTEANDO {qtdde} JOGOS', end=' ')
print('-=-' * 3)
for c in range(qtdde):
    cont = 0
    print(f'JOGO {index + 1:<3}: ', end='')
    while True:
        num = randint(1, 61)
        if num not in auxiliar:
            auxiliar.append(randint(1, 60))
            cont += 1
        if cont == 6:
            break
    jogos = auxiliar
    jogos.sort()
    auxiliar = []
    index += 1
    print(jogos)









