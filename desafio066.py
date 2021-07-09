from time import sleep
print('====== DESAFIO 066 ======')
print('-='*15)
print('Digite [ 999 ] para parar.')
print('-='*15)
sleep(1)
n = s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números, e a soma entre eles é {s}.')
