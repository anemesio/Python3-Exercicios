print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
p = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
décimo = p + (9 * razao)
for c in range(p, décimo + razao, razao):
    print(c, end = ' →  ')
print('ACABOU!')
