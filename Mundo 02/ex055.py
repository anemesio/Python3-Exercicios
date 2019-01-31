pesos = []
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa (Kg): '.format(c)))
    pesos.append(peso)
print('O maior peso lido foi  de {} Kg.'.format(max(pesos)))
print('O menor peso lido foi de {} Kg.'.format(min(pesos)))



