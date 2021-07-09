print('====== DESAFIO 089 =======')
from time import sleep
ficha = list()
while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    skip = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while skip not in 'SN':
        skip = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if skip in 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrimpe): '))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(1.5)
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
