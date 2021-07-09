print('====== DESAFIO 098 ======')
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-'*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print('-' * 30)
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont -= p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-'*30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passos: '))
contador(ini, fim, pas,)
