import random
print('Sou seu computador...\nAcabei de pensar em um número de 0 a 10.\nSerá que você consegue adivinhar qual foi?')
num = int(input('Qual é o seu palpite? '))
comp_num = random.randint(0, 10)
count = 1
while num != comp_num:
    if comp_num > num:
        print('Mais... Tente mais uma vez.')
        num = int(input('Qual é o seu palpite? '))
        count += 1
    else:
        print('Menos... Tente mais uma vez.')
        num = int(input('Qual é o seu palpite? '))
        count += 1
print('Parabé voce acertou. Foram necessárias {} tentativas.'.format(count))


