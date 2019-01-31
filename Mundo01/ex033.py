n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
numeros = [n1, n2, n3]
crecesntes = (sorted(numeros)) #Organiza a lista do menos para o maior.
print('O menor valor digitado foi {}'.format(crecesntes[0]))
print('O maior valor digitado foi {}'.format(crecesntes[2]))


