from random import randint
from time import sleep

values = []
pairs = []


def sort():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        values.append(randint(1, 9))
    for x in values:
        print(x, end=' ')
        sleep(0.5)
    print()

def sum_pairs():
    for c in values:
        if c % 2 == 0:
            pairs.append(c)
    print(f'Somando os valores pares de {values}, temos o total de {sum(pairs)}.')


sort()
sum_pairs()

