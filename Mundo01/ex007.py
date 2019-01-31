n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A média entre as notas {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, m))
if m >=7:
    print('Parabéns!! Você foi aprovado!')
else:
    print('Que pena. Você está de recuperação!')

