auxilio = []
notas = []
medias = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    auxilio.append(nome)
    auxilio.append(n1)
    auxilio.append(n2)
    notas.append(auxilio[:])
    auxilio.clear()
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 12)
print(f'{"N°":<5}{"NOME":^15}{"MÉDIA":>15}')
print('-' * 35)
for i, c in enumerate(notas):
    print(f'{i:<5}{c[0]:^15}{(c[1] + c[2]) / 2:>15.2f}')
while True:
    print('-' * 35)
    notaaluno = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    for i, c in enumerate(notas):
        if i == notaaluno:
            print(f'Notas de  {c[0]} são {c[1:]}')
    if notaaluno == 999:
        break
print('<<< VOLTE SEMPRE >>>')


