def vote(a):
    from datetime import date
    age = date.today().year - a
    if age < 16:
        print(f'Com {age} anos: NÃO VOTA.')
    elif 16 <= age < 18:
        print(f'Com {age} anos: VOTO OPCIONAL.')
    elif 18 <= age < 65:
        print(f'Com {age} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {age} anos: VOTO OPCIONAL.')


year = int(input('Em que ano você nasceu: '))
vote(year)




