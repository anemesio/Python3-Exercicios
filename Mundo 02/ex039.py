from datetime import date
ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print('\33[1;33mQuem nasceu em {} tem {} anos em {}.'.format(ano, idade, ano_atual))
if idade >= 0 and idade < 18:
    print('\33[1;36mAinda faltam {} para o alistamento.'.format(18 - idade))
    print('\33[1;36mSeu alistamento será em {}.'.format(ano_atual + (18 - idade)))
elif idade == 18:
    print('\33[1;32mVocê tem que se alistar IMEDIATAMENTE!')
else:
    print('\33[1;34mVocê já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('\33[1;34mSeu alistamento foi em {}.'.format(ano_atual - (idade - 18)))


