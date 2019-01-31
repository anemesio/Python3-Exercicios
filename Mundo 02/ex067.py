while True:
    num = int(input('Quer ver a tabuada de qual número: '))
    print('-' * 35)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c:2}')
    print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre.')


