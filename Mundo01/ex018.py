import math
ang = float(input('Digite o angulo que você deseja: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O angulo de {:.2f} tem o SENO de {:.2f}.'.format(ang, sen))
print('O angulo de {:.2f} tem o COSSENO de {:.2f}.'.format(ang, cos))
print('O angulo de {:.2f} tem a TANGENTE de {:.2f}.'.format(ang, tan))

