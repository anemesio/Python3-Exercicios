v = float(input('Qual é a velocidade atual do seu carro: ')) #Recebe a velocidade atual
if v > 80.0:
    print('MULTADO. Você excedeu o limite permitido que é de 80 Km/h.')
    multa = (v - 80) * 7.0
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia. Dirija com segurança!')