import numpy
num = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando {}! = {}'.format(num, num), end = ' x ')
list = [num, ]
while num != 1:
    num = num - 1
    list.append(num)
    print(num, end=' ')
    print(' x' if num > 1 else ' = ', end = ' ')
resultado = numpy.prod(list)
print(resultado)





