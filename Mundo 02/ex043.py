peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
IMC = peso / altura ** 2
print('O seu IMC é de {:.2f}.'.format(IMC))
if IMC < 18.5:
    print('Logo você está abaixo do peso.')
elif 18.5 <= IMC < 25:
    print('Parabéns, você está na faixa de seu peso ideal.')
elif 25 <= IMC < 30:
    print('Atenção, você está acima do seu peso ideal.')
elif 30 <= IMC < 40:
    print('Cuidado, você está na faixa de obesidade.')
else:
    print('Muito cuidado, você está na faixa de obesidade morbida.')