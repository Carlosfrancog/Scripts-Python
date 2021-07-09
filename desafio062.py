print('====== DESAFIO 061 ======')
p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = p1
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total :
        print(f'{termo} → ', end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer adicionar a mais na progreção? '))
print(f'A progreção foi finalizada com {total} termos.')
