num = int(input('Digite um número para ver sua tabuada: '))
print('-=-' * 6)
print('APRENDA A TABUADA!')
print('-=-' * 6)
for c in range(0, 11):
    print('{} x {:2} = {:2}'.format(num, c, num * c))
print('-=-' * 6)
