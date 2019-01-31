print('-' * 23)
print('Sequência de Fibonacci')
print('-' * 23)
termos = int(input('Quantos termos temos que mostrar? '))
termo1 = 0
termo2 = 1
index = 0
'''while index < (termos/2):
    print('{} → '.format(termo1), end=' ')
    termo1 += termo2
    print('{} → '.format(termo2), end=' ')
    termo2 += termo1
    index += 1
print('FIM!')'''
while index < termos:
    print('{} → '.format(termo1), end=' ')
    termo1, termo2 = termo2, termo1 + termo2
    index += 1
print('FIM!')

