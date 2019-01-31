numeros = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    if i % 2 == 1:
        impares.append(i)
print('-=-' * 15)
print(f'A lista completa é {numeros}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de impares é {impares}.')