primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
count = 1
while count <= 10:
    print('{} → '.format(termo), end=' ')
    termo += razao
    count += 1
print('PAUSA!')
count2 = 1
total = 10 #Mostra o total de termos da progressão
mais = int(input('Quantos termos você quer mostrar a mais na tela? '))
while mais != 0:
    total = total + mais
    while count2 < mais + 1:
        print('{} → '.format(termo), end=' ')
        termo += razao
        count2 += 1
    count2 = 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais na tela? '))
print('Progressão finalizada com {} termos.'.format(total))
print('FIM!!!')

'''
RESOLUÇÃO DA AULA
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print('{} → '.format(termo), end=' ')
        termo += razao
        count += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais na tela? '))
print('Progressão finalizada com {} termos.'.format(total))
'''

