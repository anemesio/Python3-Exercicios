itens = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
         'Compasso', 9.99, 'Mochila', 120, 'Canetas', 22.3, 'Livro', 34.9)
print('-' * 48)
print(f'{"Listagem de Compras":^50}')
print('-' * 48)
index = -1
x = 0
for c in itens:
    index += 1
    x += 1
    if index % 2 == 0:
        print(f'{itens[index]:.<38}R${itens[x]:>7.2f}')
print('-' * 48)


