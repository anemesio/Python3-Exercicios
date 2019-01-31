valores = []
for v in range(5):
    valor = int(input('Digite um valor: '))
    if v == 0 or valor > max(valores):
        valores.append(valor)
        print('Valor adicionado ao final da lista.')
    else:
        for i, n in enumerate(valores):
            if valor <= n:
                valores.insert(i, valor)
                print(f'Valor adicionado na posição {i} da lista.')
                break
print(f'Os valores adicionados foram {valores}.')





