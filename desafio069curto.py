print('====== DESAFIO 069 ======')
print('-='*10)
print('    CADASTRADOR   ')
print('-='*10)
idade = tot18 = totH = totM20 = 0
while True:
    print('-'*20)
    idade = int(input('Idade: '))
    if idade >= 18:
        tot18 += 1
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    if sexo == 'm':
        totH += 1
    if sexo == 'm' and idade < 20:
        totM20 += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print('-'*20)
print(f'O total de pessoas com mais de 18 anos é: {tot18}')
print(f'O total de homens cadastrados é: {totH}')
print(f'O total de mulheres cadastradas com menos de 20 é: {totM20}')
print('-'*20)
