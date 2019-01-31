print('\033[1;34m-=-\033[m' * 10)
print('\033[1;30;44mAnalisador de Trinângulos\033[m')
print('\033[1;34m-=-\033[m' * 10)
a = float(input('\033[1;33mPrimeiro segmento:\033[m '))
b = float(input('\033[1;32mSegundo segmento:\033[m'))
c = float(input('\033[1;36mTerceiro segmento:\033[m '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    if a == b == c:
        print('\033[1;34mOs segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('\033[1;34mOs segmentos acima PODEM FORMAR um triângulo ISÓCELES.')
    else:
        print('\033[1;34mOs segmentos acima PODEM FORMAR um triângulo ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

