valores = []
index = 0
for c in range(0, 5):
    valor = int(input(f'Digite um valor para a posição {index}: '))
    valores.append(valor)
    index += 1
print('-=-' * 15)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}', end='.. ')
print(f'\nO menor valor digitado foi {min(valores)} na posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}', end='.. ')

'''Para achar o indice do maior valor poderia ser usado valores.index(max(valores))'''