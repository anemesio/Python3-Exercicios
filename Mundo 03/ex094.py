pessoas = []
pessoa = {}
while True:
    pessoa['Nome'] = input('Nome: ')
    pessoa['Sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
    while pessoa['Sexo'] not in 'MF':
        print('ERRO! Por favor digite apenas M ou F.')
        pessoa['Sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Por favor digite apenas S ou N.')
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
idades = []
for i, c in enumerate(pessoas):
    idades.append(pessoas[i]['Idade'])
media = sum(idades) / len(pessoas)
print('-=-' * 18)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram:', end=' ')
for x in pessoas:
    if x['Sexo'] == 'F':
        print(x['Nome'], end='; ')
print('\nD) Lista das pessoas que tem idade acima da média:')
for x in pessoas:
    if x['Idade'] > media:
        print('   ', end='')
        for k, v in x.items():
            print(f'{k} = {v}; ',end='')
        print()
print('-=-' * 18)
print('<<< ENCERRADO >>>')

