palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMAR', 'FUTURO', 'AEIOU')
for c in palavras:
    print(f'\nNa palavra {c} temos as seguintes vogais:', end=' ')
    for x in c: # x = letra
        if x in 'AEIOUaeiou':
            if x == 'A' or x == 'a':
                print(f'\33[0;33m{x.lower()}\033[m', end=' ')
            if x == 'E' or x == 'e':
                print(f'\33[0;34m{x.lower()}\033[m', end=' ')
            if x == 'I' or x == 'i':
                print(f'\33[0;35m{x.lower()}\033[m', end=' ')
            if x == 'O' or x == 'o':
                print(f'\33[0;31m{x.lower()}\033[m', end=' ')
            if x == 'U' or x == 'u':
                print(f'\33[0;36m{x.lower()}\033[m', end=' ')
