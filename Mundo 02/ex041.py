from datetime import date
ano = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual -  ano
print('O atleta tem {} anos.'.format(idade))
categorias = ['MIRIM', 'INFANTIL', 'JÚNIOR', 'SÊNIOR', 'MASTER']
if idade <= 9:
    print('Categoria: {}.'.format(categorias[0]))
elif 9 < idade <= 14:
    print('Categoria: {}.'.format(categorias[1]))
elif 14 < idade <= 19:
    print('Categoria: {}.'.format(categorias[2]))
elif 19 < idade <= 25:
    print('Categoria: {}.'.format(categorias[3]))
else:
    print('Categoria: {}.'.format(categorias[4]))

