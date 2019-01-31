import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))
