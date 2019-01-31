from datetime import date
ano_atual = date.today().year
idades = []
for c in range(0, 7):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c + 1)))
    idade = ano_atual - ano
    idades.append(idade)
menor = 0
maior = 0
for elementos in idades:
    if elementos < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoa(s) maior(es) de idade.'.format(maior))
print('E também tivemos {} pessoa(s) menor(es) de idade.'.format(menor))

'''
RESOLUÇÃO MAIS COMPACTA
from datetime import date
ano_atual = date.today().year
menor = 0
maior = 0
for c in range(0, 7):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c + 1)))
    idade = ano_atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoa(s) maior(es) de idade.'.format(maior))
print('E também tivemos {} pessoa(s) menor(es) de idade.'.format(menor))
'''







