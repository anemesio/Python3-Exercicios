valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado. Não vou adicionar!')
    if valor not in valores:
        print('Valor adicionado com sucesso!')
        valores.append(valor)
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'Você digitou os valores: {sorted(valores)}')
