num = 0
count = 0
list = []
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    list.append(num)
    count += 1
soma = sum(list) - 999
print('Você digitou  {} números e a soma entre eles foi {}.'.format(count - 1, soma))

