frase = input('Digite um frase: ').strip().upper()
frase = frase.replace(' ', '')
inverso = (frase[::-1]) #COMANDO PARA INVERTER UMA STRING
print('O inverso {} é {}.'.format(frase, inverso))
if frase == inverso:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')


