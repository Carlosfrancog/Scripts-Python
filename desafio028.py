from random import randint
from time import sleep
print('====== DESAFIO 028 ====== ')
pc = randint(0, 5) # Faz o computador "pensar"
print('-=-'*20)
print('Eu vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-'*20)
print(' '*20)
vc = int(input('Diga em que número eu pensei! Humano.')) #jogador tenta adivinhar
print(' '*20)
print('PROCESSANDO RESULTADOS... NÃO SE AFOBE!')
sleep(2)
print(' '*20)
if pc==vc:
    print('DROGA! Voçê acertou.')
    print ( ' ' * 20 )
    print(f'O número que eu havia pensado era exatamente {pc}. Me venceu dessa vez. HUMANO!')
else:
    print('HAHAHA, parece que eu ganhei! Voçê é fraco!')
    print ( ' ' * 20 )
    print(f'Como voçê é ruim neste jogo! O número que eu havia pensado era {pc}. Treine mais!')
