print('===== DESAFIO 073 ======')
times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro',
         'Flamengo','Vasco','Chapecoense','Atlético-MG','Botafogo','Athletico-PR',
         'Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória',
         'Coritiba','Avaí','Ponte Preta','Atlético-GO')
print('-='*45)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-='*45)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-='*45)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-='*45)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-='*45)
