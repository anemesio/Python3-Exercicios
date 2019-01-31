from random import randint
print('-=-' * 9)
print('Vamos jogar PAR ou ÍMPAR!')
print('-=-' * 9)
cont = 0
while True:
    num = int(input('Digite um valor: '))
    comp = randint(0, 11) # Computador seleciona um número de 0 a 10
    total = num + comp # Soma dos números escolhidos
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? [P/I]').strip().upper()[0]
    div = total % 2 # Verifica se é par ou impar
    print('-' * 20)
    print(f'Você jogou {num} e o computador {comp}, totalizando {total}', end = ' ')
    print('que é PAR!' if div == 0 else 'que é ÍMPAR!')
    print('-' * 20)
    if div == 0:
        if escolha == 'P':
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif div != 0:
        if escolha == 'I':
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente')
    print('-=-' * 9)
print(f'GAME OVER! Você venceu {cont} vezes.')
