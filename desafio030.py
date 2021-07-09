from time import sleep
print('====== DESAFIO 030 ======')
nq = int(input('Me diga um número qualquer:')) # Vai ler um número.
print(f'AVALIANDO SE O NÚMERO {nq} É PAR ou ÍMPAR...')
sleep(1)
if nq % 2 == 0: # Se o resto da divisão for 0 o número é par.
    print(f'O NÚMERO {nq} É PAR !')
else:
    print(f'O NÚMERO {nq} É ÍMPAR!')
