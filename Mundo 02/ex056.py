idades = 0
feminino = 0
masculino =[] #Idades homens
maioridadehomem = 0 #Maior idade entre os homens
nomevelho = '' #Nome do homem mais velho
for p in range(1, 5):
    print('----- {}ª PESSOA ----- '.format(p))
    nome = (input('Nome: ')).strip()
    idade = int((input('Idade: ')))
    sexo = (input('Sexo [M/F]: ')).strip().upper()
    idades += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo == 'M' and idade > maioridadehomem:
        nomevelho = nome
    elif sexo == 'F' and idade < 20:
        feminino += 1
print('A média de idade do grupo é de {} anos.'.format(idades / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(feminino))



