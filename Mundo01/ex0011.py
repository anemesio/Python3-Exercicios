l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l * h
qtinta = a / 2
print('Sua parede tem dimensões de {}m x {}m, tendo uma área total de {:.3f}m².'.format(l, h, a))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format(qtinta))
