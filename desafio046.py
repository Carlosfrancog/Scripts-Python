from datetime import date
from time import sleep
h = date.today().year
print('====== DESAFIO 046 ======')
print('-=-'*20)
print('Contagem de 10 segundos para os fogos!!!')
for c in range(10, 0-1, -1,):
    print(c)
    sleep(1)
print(f'FELIZ {h} 🎇🎇🎇')
