def area():
    print('Controle de Terrenos')
    print('-' * 20)
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    print(f'A área de um terreno de {l:.2f} x {c:.2f} é de {l * c:.2f}m².')


area()
