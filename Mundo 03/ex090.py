aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Media'] = float(input('Média: '))
if aluno['Media'] > 5:
    aluno['Situação'] = 'APROVADO'
else:
    aluno['Situação'] = 'REPROVADO'
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')

