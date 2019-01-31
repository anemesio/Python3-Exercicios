num01 = int(input('Primeiro valor: '))
num02 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print('''\033[1;34mESCOLHA UMA DAS OPÇÕES:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR ENTRE OS DOIS
    [4] ENTRE COM NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA\033[m''')
    escolha = int(input('Qual a sua opção? '))
    if escolha == 1:
        print('O resultado de {} + {} é igual a {}.'.format(num01, num02, num01 + num02))
    elif escolha == 2:
        print('O resultado de {} x {} é igual a {}.'.format(num01, num02, num01 * num02))
    elif escolha == 3:
        lista = [num01, num02]
        lista.sort()
        print('O maior entre os números digitados é o {}.'.format(lista[1]))
    elif escolha == 4:
        num01 = int(input('Primeiro valor: '))
        num02 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa! Volte Sempre!')

