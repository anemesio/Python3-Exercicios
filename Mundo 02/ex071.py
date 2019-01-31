'''Notas de 50, 20, 10 e 1'''
print('=' * 50)
print('{:^50}'.format('BANCO PYTHON'))
print('=' * 50)
valor = int(input('Qual valor você quer sacar? R$ '))
notas = [100, 50, 20, 10, 5, 1]
for c in notas:
    n = valor // c #Calcula o número de notas de cada valor de acordo com sua posição na lista
    valor -= (n * c)
    if n > 0:
        print(f'Total de {n} cédulas de R$ {c}.')
    if valor == 0:
        break
print('=' * 50)
print('Volte sempre ao BANCO PYTHON! Tenha um Bom Dia.')











