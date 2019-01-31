from time import sleep


def maior(*valor):
    print('-=-' * 12)
    print('Analisando os valores passados:')
    sleep(1)
    for c in valor:
        print(c, end=' ')
        sleep(0.3)
    print(f'\nForam informados {len(valor)} valores.')
    sleep(1)
    print(f'O maior valor informado foi {max(valor)}.')
    sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)