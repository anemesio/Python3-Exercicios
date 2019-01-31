nome = input('Qual seu nome completo? ').strip().lower()
div = nome.split()
print('Seu nome tem Silva? {}'.format('silva' in div))
