from time import sleep
import random
print('''\033[1;34mEscolha sua jogada:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA\033[m''')
escolha = int(input('Qual é a sua jogada? '))
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
if escolha == 1:
    jogador = jogadas[0]
elif escolha == 2:
    jogador = jogadas[1]
elif escolha == 3:
    jogador = jogadas[2]
computador = random.choice(jogadas)
print('\033[1;33mJO')
sleep(0.5)
print('\033[1;33mKEN')
sleep(0.5)
print('\033[1;33mPO!!!')
sleep(0.5)
print('\033[1;35m-=-' * 10)
print('\033[1;33mComputador jogou {}.'.format(computador))
print('\033[1;34mJogador jogou {}.'.format(jogador))
print('\033[1;35m-=-' * 10)
if computador == jogador:
    print('\033[1;36mEMPATE')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print('\033[1;33mO COMPUTADOR VENCEU.\033[m')
elif computador == 'PEDRA' and jogador == 'PAPEL':
    print('\033[1;34mO JOGADOR VENCEU.\033[m')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print('\033[1;33mO COMPUTADOR VENCEU.\033[m')
elif computador == 'PAPEL' and jogador == 'TESOURA':
    print('\033[1;34mO JOGADOR VENCEU.\033[m')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print('\033[1;33mO COMPUTADOR VENCEU.\033[m')
elif computador == 'TESOURA' and jogador == 'PEDRA':
    print('\033[1;34mO JOGADOR VENCEU.\033[m')

