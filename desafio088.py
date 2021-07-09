print('====== DESAFIO 088 ======')
from random import randint
from time import sleep
jogos = list()
print(f'{"===== GERADOR DE JODOS DA MEGA SENA =====":^}')
print('-='*30)
numero_jogos = int(input('Quantiade de jogos a serem feitos: '))
print('-='*30)
for x in range(numero_jogos):
    jogos.append(list())
    for y in range(6):
        numero = randint(1, 60)
        while numero in jogos[x]:
            numero = randint(1, 60)
        jogos[x].append(numero)
    jogos[x].sort()
for x in range(numero_jogos):
    print(f'\033[32mJOGO {x+1}: {jogos[x]}\033[m')
    sleep(0.7)
print('-='*30)
print(f'\033[35mAi estão seus {x+1} jogos. Te desejo boa sorte!')

print('O PROGRAMA VAI SE ENCERRAR EM 20 SEGUNDOS!')
sleep(20)
