print('===== DESAFIO 063 ======')
t1 = 0
t2 = 1
cont = 3
num = int(input('Quantos termos você quer mostrar? '))
print(f'{t1} → ', end='')
while cont <= num:
    t3 = t1+t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
