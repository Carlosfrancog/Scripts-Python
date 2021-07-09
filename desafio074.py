print('====== DESAFIO 074 ======')
from random import randint
nuns = ((randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)))
print(f'Os números gerados foram:', end=' ')
for n in nuns:
    print(f'{n}', end=' ')
print(f'\nO maior valor gerado foi {max(nuns)}')
print(f'O menor número gerado foi {min(nuns)}')
