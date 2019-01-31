sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()[0]
if sexo == 'M':
    sexo = 'MASCULINO'
else:
    sexo = 'FEMININO'
print('Sexo {} registrado com sucesso.'.format(sexo))

