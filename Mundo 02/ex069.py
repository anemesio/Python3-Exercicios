maioridade = 0 # Recebe o número de pessoas com idades maiores a 18 anos
idade_mulheres = 0 # Recebe quantas mulheres tem menos de 20 anos
homens = 0 # Recebe a quantidade de homens cadastrados.
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
     sexo = input('Sexo [M/F]: ').strip().upper()[0]
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N]').strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        idade_mulheres += 1
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maioridade} pessoas.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {idade_mulheres} mulheres com menos de 20 anos.')
