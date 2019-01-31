valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
tempo = int(input('Quantos anos de financiamento? '))
prestacao = valor / (tempo * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(valor, tempo, prestacao))
salario30 = salario * 0.3  # 30% do salário
if prestacao > salario30:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO.')