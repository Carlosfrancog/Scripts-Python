print('====== DESAFIO 061 ======')
p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = p1
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += r
    cont += 1
print('FIM')

