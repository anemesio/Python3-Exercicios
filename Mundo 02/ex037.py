num = int(input('\33[1;34mDigite um número inteiro: '))
print('''\33[1;34mEscolha uma das bases para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL\33[m''')
opção = int(input('\33[1;34mSua opção: '))
if opção == 1:
    bin = bin(num)
    print('\33[1;33mO número em forma BINÁRIA é {}.'.format(bin)[2:])
elif opção == 2:
    oct = oct(num)
    print('\33[1;35mO número em OCTAL é {}.'.format(oct)[2:])
elif opção == 3:
    hex = hex(num)
    print('\33[1;36mO número em forma HEXAGONAL é {}.'.format(hex)[2:])
else:
    print('\33[1;31m-=-' * 7)
    print('\33[1;31mESCOLHA INVÁLIDA!!!')
    print('\33[1;31m-=-' * 7)

