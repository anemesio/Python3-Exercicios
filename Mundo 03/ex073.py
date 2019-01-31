times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético', 'Atlético-PR',
         'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense',
         'Ceará SC', 'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
print(f'Lista de Times do Brasileirão: {times}')
print('-=-' * 20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-' * 20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=-' * 20)
times_ordenados = sorted(times)
print(f'Times em ordem alfabética: {times_ordenados}')
print('-=-' * 20)
print(f'A Chapecoense terminou o campeonato na {times.index("Chapecoense") + 1}ª posição.')