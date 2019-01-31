from time import sleep


def contagem(a, b, c):
    print('-=-' * 12)
    print(f'Contagem de {a} até {b} de {c} em {c}:')
    if c < 0:
        c *= -1
    if a < b:
        while b >= a:
            print(a, end=' ')
            sleep(0.35)
            a += c
    else:
        while a >= b:
            print(a, end=' ')
            sleep(0.35)
            a -= c
    print('FIM!')


contagem(0, 10, 1)
contagem(10, 0, 2)
print('-=-' * 12)
print('Agora é sua vez de personalizar a contagem.')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)

