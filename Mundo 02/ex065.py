num = count = 0
list = []
string = ''
while string != 'N':
    num = int(input('Digite um número: '))
    list.append(num)
    count += 1
    string = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if string not in 'SN':
        while string not in 'SN':
            string = input('Entrada inválida. Digite novamente: ').strip().upper()[0]
soma = sum(list)
media = soma / count
list.sort()
menor = list[0]
maior = list[-1]
print(f'Você digitou {count} números e a média foi de {media}.')
print(f'O maior valor foi de {maior} e o menor de {menor}.')

