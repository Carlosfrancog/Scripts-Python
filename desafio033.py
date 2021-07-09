from time import sleep
print('====== DESAFIO 033 ======')
n = int(input('PRIMEIRO VALOR:'))
n2 = int(input('SEGUNDO VAlOR:'))
n3 = int(input('TERCEIRO VALOR:'))
nl = ([n, n2, n3]) # lista com os valores digitados
print('CADASTRANDO NÚMEROS...')
sleep(1)
print('-=-'*20)
print(f'Entre os números {n}, {n2} e {n3}, o maior deles é {max(nl)} . ') # max olha a lista e diz o maior
print('-=-'*20)
print(f'Entre os números {n}, {n2} e {n3}, o menor é {min(nl)} .') # min olha a lista e diz o menor

#resolução de uma maneira diferente

'''a = int(input('PRIMEIRO VALOR:'))
b = int(input('SEGUNDO VALOR:'))
c = int(input('TERCEIRO VALOR:'))
#verificando quem é maior
m = a
if b < a and b < c:
    m = b
if c < a and c < b:
    m = c
#verificando o menor
ma = a
if b > a and c > b:
    ma = b
if c > a and c > b:
    ma = c
print(f'O menor valor digitado foi {m} .')
print(f'O maior valor digitado foi {ma} .')'''
