from time import sleep
print('====== DESAFIO 031 ======')
km = float(input('De quantos KM é sua viagem?'))
print('PROCESSANDO VALORES...')
sleep(1)
c = km * 0.50
b = km * 0.45
if km >=200:
    print(f'Essa viagem de {km} km, irá custar R$ {b:.2f} .')
else:
    print(f'Essa viagem de {km} km, irá custar R$ {c:.2f} .')
    
