from time import sleep
print('====== DESAFIO 038 ======')
print(' ')
a = int(input('DIGA UM VALOR INTEIRO:'))
b = int(input('DIGA  OUTRO VALOR INTEIRO:'))
print('COMPARANDO...')
sleep(1)
if a > b:
    print('O PRIMEIRO VALOR É O MAIOR.')
elif a < b:
    print('O SEGUNDO VALOR É MAIOR.')
else:
    print('NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS.')
