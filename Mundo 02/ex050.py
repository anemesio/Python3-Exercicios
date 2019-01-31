soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite o {} valor: '.format(c + 1)))
    if n % 2 == 0:
     soma += n
     cont += 1
print('Você informou {} números PARES com soma igual a {}.'.format(cont, soma))



