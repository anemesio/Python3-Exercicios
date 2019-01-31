import random
from time import sleep
print('-=-' * 17)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('-=-' * 17)
num1 = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
num2 = random.randint(0, 5)
if num1 == num2:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(num2, num1))


