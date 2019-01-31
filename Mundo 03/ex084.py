pessoas = []
dados = []
pesos = []
maior = menor = qttde = 0
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pesos.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    qttde += 1
    resp = input('Quer continuar: [S/N] ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Quer continuar: [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 15)
print(f'Ao todo, você cadastrou {qttde} pessoas.')
maxpesos = []
minpesos = []
for p in pessoas:
    if p[1] == max(pesos):
        maxpesos.append(p[0])
    if p[1] == min(pesos):
        minpesos.append(p[0])
print(f'O maior peso foi de {max(pesos)}.Pesos de de {maxpesos}')
print(f'O menor peso foi de {min(pesos)}.Pesos de de {minpesos}')