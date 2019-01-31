d = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(d))
if d <= 200:
    print('E o preço da sua passagem será de R$ {:.2f}.'.format(d * 0.50)) #R$0,50 por Km para viagens de até 200Km.
else:
    print('E o preço da sua passagem será de R$ {:.2f}.'.format(d * 0.45)) #R$0,45 parta viagens de mais de 200Km.
