matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=-' * 15)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]}]', end='')
    print()




