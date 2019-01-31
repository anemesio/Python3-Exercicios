print('\033[1;34m-=-\033[m' * 10)
print('\033[1;30;44mAnalisador de Trinângulos\033[m')
print('\033[1;34m-=-\033[m' * 10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')



