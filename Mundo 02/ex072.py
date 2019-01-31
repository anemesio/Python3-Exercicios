numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    index = int(input('Digite um número entre 0 e 20: '))
    while index > 20:
        print('Tente novamente.', end=' ')
        index = int(input('Digite um número entre 0 e 20: '))
    for pos, c in enumerate(numeros):
        if index == pos:
            print(f'Você digitou o número {c}.')
    print('-' * 35)
    resp = input('Você quer continuar: [S/N]: ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Você quer continuar: [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break





