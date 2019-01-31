from datetime import date
trabalhador = {}
trabalhador['Nome'] = input('Nome: ')
ano = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = date.today().year - ano
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salario'] = float(input('Salário: R$ '))
    trabalhador['Aposentadoria'] = (trabalhador['Contratação'] - ano) + 35
print('-=-' * 30)
for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}.')