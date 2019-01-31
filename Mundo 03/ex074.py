from random import randint
tupla = (randint(1, 10), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11))
print('Os valores sorteados foram: ', end= '')
for c in tupla:
    print(f'{c} ', end='')
print(f'\nO maior valor digitado foi de {max(tupla)}')
print(f'O menor valor digitado foi de {min(tupla)}')
