dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preço = (dias * 60) + (km * 0.15)
print('O total a pagar pelo aluguel do carro pe de R$ {:.2f}.'.format(preço))

