valores = []
cont = 0
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    cont += 1
    resposta = input('Você quer continuar? [S/N] ').strip().upper()[0]
    if resposta not in 'SN':
        resposta = input('Você quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
print(f'Você digitou {cont} elementos.')
print('Os valores em ordem decrescente são: ', end='')
valores.sort(reverse=True)
for c in valores:
    print(c, end=' ')
if 5 in valores:
    print('\nO valor 5 faz parte da lista.')
else:
    print('\nO valor 5 não faz parte da lista.')

