nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiscúlas é ', nome.upper())
print('Seu nome em minúsculas é ', nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))
dividido = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0], nome.find(' ')))



