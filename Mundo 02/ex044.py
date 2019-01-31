from time import sleep
print('\033[1;34m====== LOJAS PYTHON =====\033[m')
valor = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:)
[1] À vista com dinheiro ou cheque;
[2] À vista no cartão;
[3] Parcelado 2x no cartão;
[4] Parcelado 3x ou mais no cartão.''')
opção = int(input('Qual é sua opção: '))
print('\033[1;34mPROCESSANDO...\033[m')
sleep(2)
if opção == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} com os 10% de DESCONTO.'.format(valor, valor * 0.9))
elif opção == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} com os 05% de DESCONTO.'.format(valor, valor * 0.95))
elif opção == 3:
    print('Sua compra de R${:.2f}, será parcelada em 2 vezes de R${:.2f} sem JUROS.'.format(valor, valor / 2))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('\033[1;34mPROCESSANDO...\033[m')
    sleep(1)
    novo_valor = valor * 1.2
    print('Sua compra será parcelada em {}x de R${:.2f} com JUROS.'.format(parcelas, novo_valor / parcelas))
    print('Sua compra de R${:.2f} custará R${:.2f} no final.'.format(valor, novo_valor))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
