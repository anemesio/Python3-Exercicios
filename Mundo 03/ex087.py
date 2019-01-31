matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
sumcoluna = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            sumcoluna += matriz[l][2]
print('-=-' * 11)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print('-=-' * 11)
print(f'A soma dos valores pares é de {pares}.')
print(f'A soma dos valores da terceira coluna é {sumcoluna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
