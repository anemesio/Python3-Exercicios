print('-' * 20)
print('LOJAS PYTHON')
print('-' * 20)
total = 0
caro = 0
qttde = 0
while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$ '))
    total += preco
    qttde += 1
    if preco > 1000:
        caro += 1
    if qttde == 1 or produto_mais_barato > preco:
        produto_mais_barato = preco
        nome_produto_mais_barato = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total da compra  foi de R$ {total:.2f}.')
print(f'Temos {caro} produto custando mais de R$ 1000.00.')
print(f'O produto mais barato foi a {nome_produto_mais_barato} que custa R$ {produto_mais_barato}.')


