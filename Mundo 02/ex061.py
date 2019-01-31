print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
p = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = p + (9 * razao)
count = 0
while p < decimo + razao:
    print(p, end=' → ')
    p = p + razao
print('FIM!!!')

#RESOLUÇÃO AULA
#primeiro = int(input('Primeiro Termo: '))
#razao = int(input('Razão: '))
#termo = primeiro
#count = 1
#while count <= 10:
#    print('{} → '.format(termo), end=' ')
#    termo += razao
#    count += 1
#print('FIM!!!')
