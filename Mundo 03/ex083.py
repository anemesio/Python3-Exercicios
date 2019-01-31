x = str(input('Digite uma expressão: ')).strip()
cont1 = 0
cont2 = 0
for c in x:
    if c == '(':
        cont1 += 1
    elif c == ')':
        cont2 += 1
if cont1 == cont2:
    print('A expressão está correta!')
else:
    print('Sua expressão está errada!')
